"""Versioned public guides and heading-level retrieval with SQLite FTS5."""
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


class Knowledge:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript('''
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS pages (
                    id INTEGER PRIMARY KEY, url TEXT UNIQUE NOT NULL, title TEXT NOT NULL,
                    markdown TEXT NOT NULL, provider TEXT, fetched_at TEXT,
                    language TEXT, stated_updated_date TEXT, sha256 TEXT, metadata TEXT);
                CREATE TABLE IF NOT EXISTS versions (
                    id INTEGER PRIMARY KEY, page_id INTEGER, markdown TEXT,
                    sha256 TEXT, fetched_at TEXT, provider TEXT);
                CREATE TABLE IF NOT EXISTS chunks (
                    id INTEGER PRIMARY KEY, page_id INTEGER, heading TEXT, body TEXT);
                CREATE INDEX IF NOT EXISTS chunks_page ON chunks(page_id);
                CREATE VIRTUAL TABLE IF NOT EXISTS search USING fts5(
                    title, heading, body, tokenize='unicode61 remove_diacritics 2');
            ''')

    def connect(self):
        db = sqlite3.connect(self.path, timeout=20)
        db.row_factory = sqlite3.Row
        return db

    def seed(self, path):
        for page in json.loads(Path(path).read_text()):
            with self.connect() as db:
                existing = db.execute('SELECT id FROM pages WHERE url=?', (page['url'],)).fetchone()
            if not existing:
                self.upsert(page)

    def upsert(self, page):
        body = page['markdown'].strip()
        if len(body) < 250:
            raise ValueError('Guide text is empty or too short to index')
        sha = hashlib.sha256(body.encode()).hexdigest()
        fields = [page['title'], body, page.get('provider', 'unknown'),
                  page.get('fetched_at', datetime.now(timezone.utc).isoformat()),
                  page.get('language', 'en'), page.get('stated_updated_date'), sha,
                  json.dumps(page.get('metadata', {}), ensure_ascii=False)]
        with self.connect() as db:
            old = db.execute('SELECT * FROM pages WHERE url=?', (page['url'],)).fetchone()
            changed = not old or old['sha256'] != sha
            if old:
                page_id = old['id']
                if changed:
                    db.execute('INSERT INTO versions(page_id,markdown,sha256,fetched_at,provider) VALUES (?,?,?,?,?)',
                               (page_id, old['markdown'], old['sha256'], old['fetched_at'], old['provider']))
                db.execute('UPDATE pages SET title=?,markdown=?,provider=?,fetched_at=?,language=?,stated_updated_date=?,sha256=?,metadata=? WHERE id=?',
                           (*fields, page_id))
                # Reindex even if only the title changed; one atomic transaction.
                db.execute('DELETE FROM search WHERE rowid IN (SELECT id FROM chunks WHERE page_id=?)', (page_id,))
                db.execute('DELETE FROM chunks WHERE page_id=?', (page_id,))
            else:
                page_id = db.execute('INSERT INTO pages(title,markdown,provider,fetched_at,language,stated_updated_date,sha256,metadata,url) VALUES (?,?,?,?,?,?,?,?,?)',
                                     (*fields, page['url'])).lastrowid
            heading, lines = page['title'], []
            sections = []
            for line in body.splitlines():
                match = re.match(r'^#{1,6}\s+(.+)', line)
                if match:
                    if lines:
                        sections.append((heading, '\n'.join(lines).strip()))
                    heading, lines = match.group(1), []
                else:
                    lines.append(line)
            if lines:
                sections.append((heading, '\n'.join(lines).strip()))
            for heading, text in sections:
                # Bound each retrieval chunk without cutting the saved full guide.
                for offset in range(0, len(text), 3500):
                    chunk = text[offset:offset + 3500].strip()
                    if not chunk:
                        continue
                    chunk_id = db.execute('INSERT INTO chunks(page_id,heading,body) VALUES (?,?,?)',
                                          (page_id, heading, chunk)).lastrowid
                    db.execute('INSERT INTO search(rowid,title,heading,body) VALUES (?,?,?,?)',
                               (chunk_id, page['title'], heading, chunk))
        return {'id': page_id, 'changed': changed}

    def retrieve(self, query, limit=6):
        # Quote all terms: user input cannot become FTS operators or SQL.
        stop = {'the','a','an','in','to','for','of','and','how','i','my','do','get','milano','milan'}
        terms = [t for t in re.findall(r'[^\W_]+', query.lower(), re.UNICODE)
                 if t not in stop and len(t) > 1][:12]
        if not terms:
            return []
        match = ' OR '.join('"' + t + '"*' for t in terms)
        with self.connect() as db:
            rows = db.execute('''SELECT p.id AS page_id,p.title,p.url,p.provider,p.fetched_at,
                p.stated_updated_date,c.heading,c.body,bm25(search,5,4,1) AS score
                FROM search JOIN chunks c ON c.id=search.rowid
                JOIN pages p ON p.id=c.page_id WHERE search MATCH ? ORDER BY score LIMIT ?''',
                              (match, min(limit, 10))).fetchall()
        return [dict(r) for r in rows]

    def read(self, page_id):
        with self.connect() as db:
            row = db.execute('SELECT id AS page_id,title,url,markdown,provider,fetched_at,stated_updated_date FROM pages WHERE id=?',
                             (page_id,)).fetchone()
        if not row:
            return {'error': 'Guide not found'}
        result = dict(row)
        result['markdown'] = result['markdown'][:22000]
        return result

    def sources(self):
        with self.connect() as db:
            return [dict(r) for r in db.execute('SELECT id,title,url,provider,fetched_at,language,stated_updated_date FROM pages ORDER BY title')]

    def export(self):
        with self.connect() as db:
            rows = [dict(r) for r in db.execute('SELECT url,title,markdown,provider,fetched_at,language,stated_updated_date,metadata FROM pages ORDER BY url')]
        for row in rows:
            row['metadata'] = json.loads(row['metadata'])
        return rows

    def stats(self):
        with self.connect() as db:
            return {'pages': db.execute('SELECT count(*) FROM pages').fetchone()[0],
                    'sections': db.execute('SELECT count(*) FROM chunks').fetchone()[0],
                    'providers': {r[0]: r[1] for r in db.execute('SELECT provider,count(*) FROM pages GROUP BY provider')}}

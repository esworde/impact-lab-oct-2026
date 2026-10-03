"""Refresh curated student guides via Firecrawl, retaining failed pages' previous versions."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from urllib.parse import urlparse

from dotenv import load_dotenv
import httpx

from webapp.knowledge import Knowledge
from webapp.personas import PERSONA_GUIDES
from webapp.howto import CATALOG

APPROVED_HOSTS = {'studyandwork.yesmilano.it', 'www.yesmilano.it', 'www.comune.milano.it', 'servizicrm.comune.milano.it', 'italiana.esteri.it'}

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT.parent / '.env')
BASE = 'https://studyandwork.yesmilano.it'
GUIDES = [
    'https://italiana.esteri.it/italiana/opportunity/studying-in-italy/visas-and-permits/',
    BASE + '/en/study/how-to/first-steps',
    BASE + '/en/study/how-to/rents',
    BASE + '/en/study/how-to/take-residence-milano-students',
    BASE + '/en/study/how-to/student-visa',
    BASE + '/en/study/how-to/residence-permit-students',
    BASE + '/en/study/how-to/get-italian-tax-code-codice-fiscale',
    BASE + '/en/study/how-to/get-your-student-transportation-pass',
    BASE + '/en/study/how-to/national-health-service-students-step-step',
    BASE + '/en/study/how-to/get-temporary-residence-milano',
    BASE + '/en/study/how-to/spid',
    BASE + '/en/study/how-to/id-card',
    BASE + '/en/study/how-to/patronato',
    BASE + '/en/study/how-to/scolarships-and-study-grants',
    BASE + '/en/study/packing/universitaly',
    BASE + '/en/international-student-desk',
    BASE + '/en/study/best-places-study-milano',
    BASE + '/en/work/getting-started-guide/learn-italian',
    'https://www.comune.milano.it/servizi/anagrafe/cambio-di-residenza',
    'https://www.comune.milano.it/servizi/tributi/tari-dichiarazione-di-occupazione-di-appartamenti-e-immobili',
    'https://www.comune.milano.it/servizi/anagrafe/certificati-anagrafici',
]

GUIDES = list(dict.fromkeys([entry['indexed_url'] for entry in CATALOG] + GUIDES))


def scrape(url, api_key):
    parsed = urlparse(url)
    if parsed.scheme != 'https' or parsed.hostname not in APPROVED_HOSTS:
        raise ValueError('Only approved public source hosts can be indexed')
    payload = {'url': url, 'formats': ['markdown', 'links'], 'maxAge': 0,
               'onlyMainContent': True, 'timeout': 60000}
    if parsed.hostname == 'studyandwork.yesmilano.it':
        payload.update({'onlyMainContent': False, 'includeTags': ['article'],
                        'excludeTags': ['nav', 'footer']})
    with httpx.Client(timeout=95) as client:
        response = client.post('https://api.firecrawl.dev/v2/scrape', json=payload,
                               headers={'Authorization': 'Bearer ' + api_key})
        response.raise_for_status()
        result = response.json()
    if not result.get('success'):
        raise ValueError('Firecrawl did not return a successful scrape')
    data = result['data']
    meta = data.get('metadata', {})
    markdown = data.get('markdown', '').strip()
    if meta.get('statusCode', 200) >= 400 or len(markdown) < 300 or re.search(r'^#?\s*(403|Forbidden|Access denied)', markdown, re.I):
        raise ValueError('Origin blocked or returned insufficient guide text')
    # A changed origin URL must remain an approved public source.
    canonical = meta.get('url') or meta.get('sourceURL') or url
    if urlparse(canonical).hostname not in APPROVED_HOSTS:
        raise ValueError('Unexpected redirect outside approved hosts')
    if urlparse(canonical).path in {'', '/'} and parsed.path not in {'', '/'}:
        raise ValueError('Guide redirected to a homepage')
    if parsed.hostname == 'servizicrm.comune.milano.it':
        article = re.search(r'^## [^\n]+\n', markdown, re.M)
        end = re.search(r'Ultimo aggiornamento:\s*\d{2}/\d{2}/\d{4}', markdown)
        if not article or not end or end.end() < article.start():
            raise ValueError('Municipal FAQ article could not be isolated')
        markdown = markdown[article.start():end.end()].strip()
    markdown = markdown.split('### Join our Community!')[0].strip()
    updated = re.search(r'(?:Last updated|Ultimo aggiornamento):\s*(\d{2}/\d{2}/\d{4})', markdown)
    return {'url': url, 'title': meta.get('title', url).split(' | ')[0], 'markdown': markdown,
            'provider': 'firecrawl', 'fetched_at': datetime.now(timezone.utc).isoformat(),
            'language': meta.get('language', 'en'), 'stated_updated_date': updated.group(1) if updated else None,
            'metadata': {'origin_url': canonical, 'status_code': meta.get('statusCode'),
                         'links': data.get('links', []), 'published_time_unverified': meta.get('publishedTime')}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=39)
    parser.add_argument('--url', action='append')
    parser.add_argument('--snapshot', action='store_true', help='Update deployable public-content seed JSON')
    args = parser.parse_args()
    key = os.getenv('FIRECRAWL_API_KEY')
    if not key:
        raise SystemExit('FIRECRAWL_API_KEY must be configured in .env')
    knowledge = Knowledge(os.getenv('DATABASE_PATH', str(ROOT / 'data/knowledge.sqlite')))
    knowledge.seed(ROOT / 'data/seed.json')
    rental_file = ROOT / 'data/rental-links.json'
    rentals = json.loads(rental_file.read_text()) if rental_file.exists() else []
    urls = list(dict.fromkeys(args.url or GUIDES + PERSONA_GUIDES + rentals))[:max(1, min(args.limit, 60))]
    report = {'started_at': datetime.now(timezone.utc).isoformat(), 'success': [], 'errors': []}
    with ThreadPoolExecutor(max_workers=3) as pool:
        jobs = {pool.submit(scrape, url, key): url for url in urls}
        for job in as_completed(jobs):
            url = jobs[job]
            try:
                page = job.result()
                saved = knowledge.upsert(page)
                report['success'].append({'url': url, 'title': page['title'], **saved})
                print('Indexed:', page['title'], flush=True)
            except Exception as exc:
                # Never output API keys or full request headers.
                report['errors'].append({'url': url, 'error': type(exc).__name__})
                print('Not indexed:', url, type(exc).__name__, flush=True)
    report['finished_at'] = datetime.now(timezone.utc).isoformat()
    (ROOT / 'data/ingest-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    if args.snapshot:
        (ROOT / 'data/seed.json').write_text(json.dumps(knowledge.export(), ensure_ascii=False, indent=2))
    print(json.dumps({'indexed': len(report['success']), 'failed': len(report['errors']), **knowledge.stats()}))
    if not report['success']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

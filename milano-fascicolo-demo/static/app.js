const $ = (id) => document.getElementById(id);
const labels = {
  disconnected: 'Non collegato', starting: 'Avvio del browser...',
  waiting_login: 'Browser aperto: completa l’accesso con SPID/CIE',
  authenticated: 'Accesso completato', fetching: 'Recupero pagamenti...',
  done: 'Pagamenti recuperati', error: 'Errore'
};
let busy = false;
let previousPayments = '';
function normalizePayment(payment) {
  // Handle collected cards whose labelled fields were normalized before the
  // title/status selectors were available. Only the verified card format applies.
  const result = {...payment};
  const lines = (payment.raw_text || '').split('\n').map(line => line.trim()).filter(Boolean);
  if (payment.date && payment.amount && lines.length >= 5 &&
      ['pagato', 'da pagare', 'scaduto', 'in corso', 'annullato'].includes(lines[2].toLowerCase())) {
    result.description ??= lines[1];
    result.status ??= lines[2];
  }
  return result;
}
function render(data) {
  $('mode').textContent = data.mock ? 'Mock · dati di esempio' : 'Browser-assisted demo';
  $('status').textContent = data.mock && ['starting', 'waiting_login'].includes(data.state) ? 'Simulazione dell’accesso...' : labels[data.state];
  $('message').textContent = data.message;
  $('dot').className = data.state;
  $('connect').disabled = busy || data.state !== 'disconnected';
  $('disconnect').disabled = busy || data.state === 'disconnected';
  $('resume').hidden = !data.can_resume;
  $('resume').textContent = data.state === 'waiting_login' ? 'Verifica accesso' : data.state === 'done' ? 'Aggiorna pagamenti' : 'Riprendi';
  $('resume').disabled = busy;
  const rows = data.payments.map(normalizePayment);
  $('results').hidden = rows.length === 0;
  $('empty').hidden = rows.length > 0;
  $('empty').textContent = data.state === 'done' ? 'Nessun pagamento presente nella vista corrente.' : 'I pagamenti appariranno qui dopo il recupero.';
  $('count').textContent = data.state === 'done' ? `${rows.length} ${rows.length === 1 ? 'pagamento' : 'pagamenti'}` : '—';
  const serialized = JSON.stringify(rows);
  if (serialized === previousPayments) return;
  previousPayments = serialized;
  $('payments').replaceChildren();
  for (const payment of rows) {
    const tr = document.createElement('tr');
    for (const key of ['date', 'description', 'amount', 'status']) {
      const td = document.createElement('td');
      td.textContent = payment[key] ?? '—'; // Portal text is never HTML.
      if (key === 'description' && payment.raw_text) {
        const details = document.createElement('details');
        const summary = document.createElement('summary');
        summary.textContent = 'Testo originale';
        const raw = document.createElement('p');
        raw.textContent = payment.raw_text;
        details.append(summary, raw);
        td.append(details);
      }
      tr.append(td);
    }
    $('payments').append(tr);
  }
}
async function request(path, method = 'GET') {
  const response = await fetch(`/api/${path}`, {method, cache: 'no-store', headers: {'X-Demo-Request': '1'}});
  if (!response.ok) throw new Error('Richiesta non riuscita. Riprova o ricarica la pagina.');
  return response.json();
}
function offline(error) {
  $('status').textContent = 'Errore';
  $('message').textContent = `${error.message} Controlla che il server locale sia in esecuzione.`;
  $('dot').className = 'error';
  $('payments').replaceChildren();
  previousPayments = '';
  $('results').hidden = true;
  $('empty').hidden = false;
  $('empty').textContent = 'Connessione al server non disponibile.';
  $('count').textContent = '—';
  $('connect').disabled = $('disconnect').disabled = $('resume').disabled = true;
}
for (const action of ['connect', 'resume', 'disconnect']) {
  $(action).addEventListener('click', async () => {
    busy = true;
    $('connect').disabled = $('disconnect').disabled = $('resume').disabled = true;
    try { const data = await request(action, 'POST'); busy = false; render(data); }
    catch (error) { busy = false; offline(error); }
  });
}
async function poll() {
  if (!busy) {
    try { const data = await request('status'); if (!busy) render(data); }
    catch (error) { if (!busy) offline(error); }
  }
  setTimeout(poll, 750);
}
poll();

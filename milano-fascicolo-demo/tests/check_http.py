"""Run against the MOCK server on 127.0.0.1:8000; uses only Python stdlib."""
import json
import time
import urllib.error
import urllib.request


def check(path, method="GET", headers=None, expected=200):
    req = urllib.request.Request("http://127.0.0.1:8000" + path,
                                 method=method, headers=headers or {})
    try:
        response = urllib.request.urlopen(req, timeout=5)
    except urllib.error.HTTPError as error:
        response = error
    assert response.status == expected, (path, response.status)
    return response


assert json.load(check("/api/status"))["mock"], "Use MOCK_MODE=true server"
for path in ["/", "/static/style.css", "/static/app.js", "/api/status"]:
    assert check(path).headers["Cache-Control"] == "no-store"
check("/api/connect", "POST", expected=403)
check("/api/connect", "POST", {"X-Demo-Request": "1", "Origin": "https://example.org"}, 403)
check("/api/status", headers={"Host": "example.org"}, expected=400)
check("/api/status", headers={"Sec-Fetch-Site": "cross-site"}, expected=403)
headers = {"X-Demo-Request": "1"}
check("/api/disconnect", "POST", headers)
check("/api/connect", "POST", headers, 202)
check("/api/connect", "POST", headers, 409)
for _ in range(50):
    data = json.load(check("/api/status"))
    if data["state"] == "done":
        break
    time.sleep(0.1)
assert data["state"] == "done"
assert len(data["payments"]) == 2
assert data["payments"][0]["amount"] == "€ 125,00"
check("/api/resume", "POST", headers, 202)
check("/api/disconnect", "POST", headers)
data = json.load(check("/api/status"))
assert data["state"] == "disconnected" and data["payments"] == []
print("PASS: HTTP, mock flow, duplicate connect, clearing data, origin/host restrictions and no-store.")

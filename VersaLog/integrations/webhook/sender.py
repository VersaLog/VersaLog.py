import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def send_json(url, payload, timeout=3.0, headers=None):
    request_headers = {
        "Content-Type": "application/json",
        "User-Agent": "VersaLog/3.0",
    }

    if headers:
        request_headers.update(headers)

    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    request = Request(
        url,
        data=data,
        headers=request_headers,
        method="POST",
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            return 200 <= response.status < 300

    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"[Webhook HTTP Error] status={e.code}, reason={e.reason}")
        print(f"[Webhook Response] {body}")
        return False

    except (URLError, TimeoutError, OSError, ValueError) as e:
        print(f"[Webhook Connection Error] {type(e).__name__}: {e}")
        return False
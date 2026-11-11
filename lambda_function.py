import json
import os
from urllib.request import Request, urlopen


def lambda_handler(event, context):
    issue = event.get("issue")
    if event.get("action") not in (None, "opened") or not isinstance(issue, dict):
        return "ignored"

    url = issue.get("html_url")
    if not isinstance(url, str) or not url.startswith("https://github.com/"):
        return "ignored"

    payload = json.dumps({"text": f"Issue Created: {url}"}).encode("utf-8")
    request = Request(
        os.environ["SLACK_URL"],
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=5) as response:
        return response.read().decode("utf-8")

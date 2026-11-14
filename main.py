
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr
from pathlib import Path
import re

def analyze_email(file_path):
    print("Reading file:", file_path)

    with open(file_path, "rb") as file:
        msg = BytesParser(
            policy=policy.default
        ).parse(file)

    sender = parseaddr(str(msg.get("From", "")))[1]
    reply_to = parseaddr(str(msg.get("Reply-To", "")))[1]
    subject = str(msg.get("Subject", ""))

    indicators = []

    if reply_to and sender.lower() != reply_to.lower():
        indicators.append("Sender and Reply-To mismatch")

    if "urgent" in subject.lower():
        indicators.append("Urgency language in subject")

    body = msg.get_body(preferencelist=("plain",))
    content = body.get_content() if body else ""

    if re.search(
        r"http://\d{1,3}(?:\.\d{1,3}){3}",
        content
    ):
        indicators.append("IP-based HTTP link")

    score = min(len(indicators) * 25, 100)

    print("\n=== Phishing Detection Report ===")
    print("Sender:", sender)
    print("Reply-To:", reply_to)
    print("Subject:", subject)
    print("Indicators:", indicators)
    print("Risk Score:", score, "/ 100")


if __name__ == "__main__":
    sample = Path(__file__).resolve().parent / "sample.eml"
    analyze_email(sample)

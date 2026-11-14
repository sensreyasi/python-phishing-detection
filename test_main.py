
from pathlib import Path
from main import analyze_email

def test_phishing_email(capsys):
    sample = Path(__file__).parent / "sample.eml"

    analyze_email(sample)

    output = capsys.readouterr().out

    assert "Sender and Reply-To mismatch" in output
    assert "Urgency language in subject" in output
    assert "IP-based HTTP link" in output
    assert "Risk Score: 75 / 100" in output

def test_legitimate_email(capsys):
    sample = Path(__file__).parent / "legitimate.eml"

    analyze_email(sample)

    output = capsys.readouterr().out

    assert "Indicators: []" in output
    assert "Risk Score: 0 / 100" in output



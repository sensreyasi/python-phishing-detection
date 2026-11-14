# Python Phishing Detection Tool

A beginner-friendly cybersecurity project that analyzes `.eml` email files for suspicious indicators using Python.

## Project Overview

This tool uses rule-based analysis to identify common phishing warning signs in email headers, subjects, and message content.

It is designed as an educational cybersecurity portfolio project to demonstrate email analysis, Python programming, basic threat detection, and automated testing.

## Features

- Parses email headers and message content.
- Detects mismatches between the `From` and `Reply-To` addresses.
- Identifies urgency language in email subjects.
- Flags HTTP links containing IPv4-style addresses.
- Generates a simple risk score from 0 to 100.
- Supports automated testing with pytest.

## Technologies Used

- Python
- Python standard library (`email`, `pathlib`, `re`)
- pytest
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
python-phishing-detection/
├── main.py
├── sample.eml
├── legitimate.eml
├── test_main.py
├── .gitignore
└── README.md
```

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/sensreyasi/python-phishing-detection.git
cd python-phishing-detection
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install pytest for testing:

```bash
python -m pip install pytest
```

## Usage

Run the phishing detection tool against the included synthetic sample:

```bash
python main.py
```

Expected detection indicators:

```text
Sender and Reply-To mismatch
Urgency language in subject
IP-based HTTP link
Risk Score: 75 / 100
```

## Automated Testing

Run:

```bash
python -m pytest -v
```

The initial test suite covers:

1. A synthetic suspicious email with three indicators.
2. A legitimate-looking email with no triggered indicators.

Both tests passed during local development.

## Detection Methodology

The tool currently applies three heuristic checks:

| Indicator | Condition | Score |
|---|---|---|
| Sender mismatch | `From` differs from `Reply-To` | +25 |
| Urgent subject | Subject contains `urgent` | +25 |
| IP-based HTTP link | Body contains an HTTP URL beginning with an IPv4-style address | +25 |

The total is capped at 100.

## Limitations

- Risk scores are heuristic values, not phishing probabilities.
- Detection rules are intentionally simple and may produce false positives or false negatives.
- The tool does not verify SPF, DKIM, or DMARC.
- It does not perform live URL reputation checks.
- The current command-line entry point analyzes the bundled `sample.eml` file.
- The tool is not suitable as a standalone production email security solution.

## Security Considerations

All included email samples are synthetic. The project uses reserved example domains and documentation IP addresses. Do not publish real emails containing personal information, credentials, or sensitive organizational data.

## Skills Demonstrated

- Email header analysis
- Phishing indicator identification
- Python scripting
- Regular expressions
- Rule-based risk scoring
- Automated testing with pytest
- Cybersecurity project documentation

## Future Improvements

- Add command-line arguments for analyzing different email files.
- Extract and inspect URLs more robustly.
- Add HTML email support.
- Introduce configurable detection rules.
- Expand test coverage with additional benign and suspicious examples.

## Disclaimer

This project is for educational and defensive cybersecurity purposes only.

# Python Phishing Detection Tool

A beginner-friendly cybersecurity project that analyzes `.eml` email files for suspicious indicators using Python.

## What Is This Project?

This is a Python-based, command-line phishing email detection prototype. It reads a bundled synthetic `.eml` email, examines selected email headers, subject text, and plain-text content, then reports suspicious indicators and a rule-based risk score.

The project demonstrates an introductory approach to email threat triage rather than a production-ready phishing filter.

## Why I Built This Project

I built this project to turn cybersecurity concepts into a practical, demonstrable tool. Phishing is a common way attackers try to trick people into revealing information or visiting malicious websites, and I wanted hands-on experience analyzing email warning signs instead of only learning about them theoretically.

I also wanted to strengthen my Python scripting, email-header analysis, automated testing, and GitHub workflow skills while creating a project that employers can review.

## What Problem Am I Trying to Solve?

Suspicious emails can look convincing at first glance, and manually reviewing their headers, wording, and links takes time. A beginner analyst needs a repeatable way to surface basic warning signs for further investigation.

This prototype addresses that need by automatically highlighting three specific indicators in a sample email. It **does not determine conclusively whether an email is phishing**; it provides simple evidence to support manual review.

## How I Solve It

1. **Parse the email:** Python's `email` library reads the `.eml` file and extracts the sender, Reply-To address, subject, and plain-text body.
2. **Apply detection rules:** The script checks for a mismatch between sender and Reply-To addresses, the word `urgent` in the subject, and an HTTP link beginning with an IPv4-style address.
3. **Assign a risk score:** Each triggered rule contributes 25 points. This is an illustrative heuristic score, not a probability or validated severity rating.
4. **Display the findings:** The command-line report lists the relevant email fields, triggered indicators, and total score.
5. **Test the behavior:** Two pytest tests check the output for synthetic suspicious and legitimate-looking examples. GitHub Actions runs the test suite on Python 3.9 and 3.12 whenever code is pushed or a pull request is opened.

For the included suspicious sample, all three rules trigger, resulting in a score of **75/100**. The legitimate-looking sample triggers none, resulting in **0/100**.

## Tools and Technologies

| Tool | How I Used It |
|---|---|
| **Python** | Implemented email parsing, detection rules, and scoring |
| **Python standard library** (`email`, `re`, `pathlib`) | Parsed email files, matched URL patterns, and located the sample file |
| **pytest** | Automated checks for suspicious and legitimate-looking sample emails |
| **GitHub Actions** | Continuous integration testing on Python 3.9 and 3.12 |
| **Visual Studio Code** | Developed and ran the project locally |
| **Git and GitHub** | Version control, documentation, and public project hosting |

## Results and What I Learned

- Built a working rule-based email analysis prototype with readable command-line output.
- Verified both sample scenarios locally using pytest.
- Configured GitHub Actions; the Python 3.9 and 3.12 jobs both passed in workflow run #2.
- Practiced interpreting email headers, designing explainable detection rules, documenting limitations, and troubleshooting a CI environment compatibility issue.

**Scope:** The examples are synthetic. The tool does not inspect arbitrary emails through its current command-line entry point, check sender authentication, evaluate URL reputation, or guarantee phishing detection.

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
├── .github/
│   └── workflows/
│       └── python-tests.yml
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

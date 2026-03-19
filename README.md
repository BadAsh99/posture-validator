# posture-validator

> AI-powered PAN-OS security posture assessment tool using Google Gemini

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![Palo Alto](https://img.shields.io/badge/Palo_Alto-PAN--OS-orange)

---

## Overview

A web-based security posture assessment tool for **Palo Alto Networks PAN-OS configurations**. Upload a firewall config (XML or JSON), and Gemini AI analyses it against security best practices — generating a structured findings report with severity-categorised issues and actionable recommendations.

Designed for security engineers who need to rapidly audit PAN-OS deployments, validate inherited configurations, or produce audit-ready reports without manually parsing config files.

---

## Architecture

```
Streamlit UI
    │
    ├── File Upload (XML / JSON)
    │       └── Config parsing + context extraction
    │
    ├── Prompt Builder
    │       └── System prompt + config context + analysis request
    │
    └── Gemini API (generativelanguage.googleapis.com)
            └── AI security analysis
                    │
                    ├── Markdown summary report
                    ├── Issues table (severity-tagged)
                    └── CSV download
```

---

## Features

- **Drag-and-drop config upload** — PAN-OS XML and JSON configuration formats
- **AI-driven analysis** — Gemini evaluates configs against PAN-OS security best practices
- **Structured output** — findings categorised by severity: Critical, High, Medium, Low
- **Markdown report** — human-readable summary with recommendations
- **CSV export** — downloadable issues table for tracking and audit records
- **Application Default Credentials** — no hardcoded API keys required

---

## Example Output

```
CRITICAL: Management interface accessible from 0.0.0.0/0
  → Restrict management access to specific admin source IPs

HIGH: Security policy contains "any" application rules
  → Replace with application-specific allow rules

MEDIUM: Anti-spyware profile not applied to outbound rules
  → Attach threat prevention profile to all internet-bound policies

LOW: Log forwarding profile missing on internal trust rules
  → Add log forwarding to maintain full audit trail
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| UI | Streamlit |
| AI | Google Gemini API |
| Backend | Python 3.12 |
| Data | Pandas |
| Auth | Google Application Default Credentials |

---

## Getting Started

```bash
git clone https://github.com/BadAsh99/posture-validator.git
cd posture-validator
python3 -m venv .venv && source .venv/bin/activate
pip install streamlit pandas requests
```

### Authenticate

```bash
gcloud auth application-default login
# or set GOOGLE_API_KEY in .env
```

### Run

```bash
streamlit run posture_validator.py
```

---

## Supported Config Formats

- PAN-OS full XML export (`File > Export > Running Config`)
- Partial XML (specific sections)
- JSON-formatted configuration exports

---

## Related

- **[Firewise AI](https://github.com/BadAsh99/firewise-ai)** — interactive Q&A version with Gemini + GPT-4 toggle and streaming responses

---

## Author

**Ash Clements** — Sr. Principal Security Consultant | Cloud & AI Security | Palo Alto Networks Specialist
[github.com/BadAsh99](https://github.com/BadAsh99)

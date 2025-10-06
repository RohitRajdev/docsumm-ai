# docsumm-ai
One-line document summarizer for PDFs, Word, or text — optimized for context retention, not token count.


[![CI](https://github.com/RohitRajdev/docsumm-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/RohitRajdev/docsumm-ai/actions/workflows/ci.yml)
![PyPI](https://img.shields.io/badge/pypi-soon-blue)
![License](https://img.shields.io/badge/license-MIT-informational)

**Audience-aware document summarizer (PDF/DOCX/TXT).**  
Optimized for context retention, not token count. Generate different summaries for **exec**, **engineer**, or **legal** audiences with one command.

---

## Install
*(publishing to PyPI next — for now clone/`pip install -e .` or use as a module)*

```bash
# local dev install
pip install -U pip
pip install -e .

-------

## Quickstart (CLI)
docsumm --in path/to/contract.pdf --audience legal --purpose risks --out summary.md

-----

## Quickstart (Python)
from docsumm_ai import summarize, SummaryConfig

text = summarize(
    "path/to/report.txt",
    SummaryConfig(audience="exec", purpose="brief")
)
print(text)

-----

## What it does (v0.1)

Reads TXT (PDF/DOCX coming next commits)

Audience & purpose templates (exec / engineer / legal × brief / risks / actions)

Returns a clean, bullet-style summary

Simple CLI + Python API

------

## Roadmap

 PDF + DOCX parsing (with structure hints)

 Local & API LLM routing (Ollama/OpenAI via extras)

 Streamlit app for upload + audience switcher

 Evaluation harness and example datasets

## License

MIT © Rohit Rajdev

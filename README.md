# docsumm-ai  
**One-line, opinionated document summarizer for PDFs, Word, or text — optimized for context retention, not token count.**

![CI](https://github.com/RohitRajdev/docsumm-ai/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11%20|%203.12-blue)
![Version](https://img.shields.io/badge/version-0.1.0-orange)

---

## Why docsumm-ai?

Summarizing long documents shouldn’t mean losing meaning.  
Most tools today **truncate context** just to fit into token limits — resulting in shallow, inaccurate summaries.

`docsumm-ai` was built to fix that.

We designed it for **researchers, analysts, and AI developers** who care about both **fidelity and efficiency**.  
It automatically adapts to document structure, ensuring retention of key insights from text, Word, or PDFs — in a single line.

---

## What Makes It Different

✅ **One-line summarize()** — clean summaries with context retention  
✅ **Handles PDFs, DOCX, TXT** — no format left behind  
✅ **Context-aware chunking** — semantic segmentation, not blind splitting  
✅ **Adaptive compression** — keeps the right level of detail per section  
✅ **CLI + Python API** — works both in scripts and terminal  
✅ **Transparent JSON + Markdown output** — reproducible and human-readable  

---

## Installation

```bash
pip install docsumm-ai

## Quickstart
1. Summarize a text file
from docsumm_ai import summarize

summary = summarize("annual_report.txt", mode="concise")
print(summary)

2. Summarize a PDF (CLI)
docsumm summarize my_report.pdf --mode detailed --out summary.md

## Output Example

Input:

“The study explores the correlation between urban growth and environmental impact across 32 global cities…”

Output:

“Analyzes 32 cities showing urban expansion drives higher emissions; highlights need for adaptive policies.”

🪪 License

MIT License © 2025 Rohit Rajdev
Open for community collaboration and research integration.

🌐 Links

🔗 GitHub: https://github.com/RohitRajdev/docsumm-ai

✉️ Contact: rohitrajdev.com

🧠 Related project: dataprep-ai

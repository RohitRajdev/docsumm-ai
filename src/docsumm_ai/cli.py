
import argparse
from .core import summarize, SummaryConfig

def main():
    ap = argparse.ArgumentParser(prog="docsumm", description="Audience-aware document summarizer")
    ap.add_argument("--in", dest="inp", required=True, help="Input file (txt/pdf/docx)")
    ap.add_argument("--audience", default="exec", choices=["exec", "engineer", "legal"])
    ap.add_argument("--purpose", default="brief", choices=["brief", "risks", "actions"])
    ap.add_argument("--out", default=None, help="Write summary to this file")
    args = ap.parse_args()

    text = summarize(args.inp, SummaryConfig(audience=args.audience, purpose=args.purpose))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)

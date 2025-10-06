from dataclasses import dataclass
from pathlib import Path

@dataclass
class SummaryConfig:
    audience: str = "exec"     # exec|engineer|legal
    purpose: str = "brief"     # brief|risks|actions
    model: str = "local:mistral"  # placeholder for future routing

_AUDIENCE_HINTS = {
    "exec": "Be concise. Focus on outcomes, risks, and decisions.",
    "engineer": "Emphasize technical details, assumptions, and dependencies.",
    "legal": "Highlight obligations, liabilities, exceptions, and risk language.",
}

_PURPOSE_HINTS = {
    "brief": "Provide a high-level summary with key points.",
    "risks": "List major risks/concerns and potential mitigations.",
    "actions": "List recommended actions, owners, and timelines if present.",
}

def _read_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    # MVP: txt only (PDF/DOCX coming next)
    if p.suffix.lower() in {".txt", ""}:
        return p.read_text(encoding="utf-8", errors="ignore")
    # Fallback: read raw - you’ll replace with PDF/DOCX readers shortly
    return p.read_text(encoding="utf-8", errors="ignore")

def _prompt(audience: str, purpose: str, content: str) -> str:
    ah = _AUDIENCE_HINTS.get(audience, _AUDIENCE_HINTS["exec"])
    ph = _PURPOSE_HINTS.get(purpose, _PURPOSE_HINTS["brief"])
    return (
        f"Audience: {audience}\nPurpose: {purpose}\n"
        f"Guidance: {ah} {ph}\n\n"
        f"Document:\n{content}\n"
        "----\n"
        "Return a concise bullet list (5-12 bullets) capturing the most useful points.\n"
    )

def summarize(path: str, cfg: SummaryConfig = SummaryConfig()) -> str:
    """
    MVP: heuristic 'summary' — first N lines cleaned into bullets.
    Next commit: route prompt to an LLM (local/API) and return generated summary.
    """
    content = _read_text(path)
    prompt = _prompt(cfg.audience, cfg.purpose, content)  # not used yet; reserved

    lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
    chosen = lines[:12] if lines else []
    bullets = ["- " + ln for ln in chosen]
    if not bullets:
        bullets = ["- (file contained no extractable text)"]
    return "\n".join(bullets)


from docsumm_ai import summarize, SummaryConfig

def test_smoke():
    # simple in-memory temp file
    import tempfile, os
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as f:
        f.write("Line one\nLine two\nLine three\n")
        name = f.name
    try:
        out = summarize(name, SummaryConfig(audience="exec", purpose="brief"))
        assert "- Line one" in out
    finally:
        os.remove(name)


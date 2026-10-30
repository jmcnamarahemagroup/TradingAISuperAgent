"""Knowledge ingestion from /learning with simple search (embeddings optional)."""
import os
from pathlib import Path
from typing import List, Dict


def ingest_learning_notes(learning_dir: str = "learning") -> List[Dict]:
    """Ingest txt/md files, keep provenance."""
    notes = []
    p = Path(learning_dir)
    if not p.exists():
        return notes
    for f in p.rglob("*.*"):
        if f.suffix.lower() in {".txt", ".md"}:
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
                notes.append({
                    "path": str(f),
                    "content": text,
                    "mtime": f.stat().st_mtime,
                })
            except Exception:
                continue
    return notes


def simple_search(notes: List[Dict], query: str, top_k: int = 5) -> List[Dict]:
    """Basic keyword search with provenance."""
    q = query.lower()
    results = []
    for n in notes:
        if q in n["content"].lower():
            snippet = n["content"][:300] + "..." if len(n["content"]) > 300 else n["content"]
            results.append({"path": n["path"], "snippet": snippet, "score": 1.0})
    return results[:top_k]

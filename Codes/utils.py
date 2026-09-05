from pathlib import Path
import json


def load_json(path):
    path = Path(path)
    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_documents(folder):
    documents = []

    folder = Path(folder)

    if not folder.exists():
        return documents

    for file in folder.rglob("*"):
        if file.suffix.lower() in [".md", ".txt"]:
            documents.append({
                "name": file.name,
                "path": str(file),
                "content": file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            })

    return documents

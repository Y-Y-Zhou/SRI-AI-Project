from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

PINE_RIDGE_CORPUS = DATA_DIR / "pine_ridge_corpus"
SOURCE_REGISTRY = DATA_DIR / "metadata" / "source_registry.json"
ACCESS_MATRIX = DATA_DIR / "metadata" / "access_matrix.json"

DEFAULT_ROLE = "Executive"

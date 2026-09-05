from utils import load_json
from config import SOURCE_REGISTRY


class MetadataManager:

    def __init__(self):
        self.sources = load_json(SOURCE_REGISTRY)

    def get_source(self, filename):
        return self.sources.get(filename, {})

    def is_approved(self, filename):
        source = self.get_source(filename)
        return source.get("approval_status") == "Approved"

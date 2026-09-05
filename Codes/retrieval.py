from document_processor import DocumentProcessor
from metadata import MetadataManager


class Retriever:

    def __init__(self, corpus_path):
        self.documents = DocumentProcessor(corpus_path).process()
        self.metadata = MetadataManager()

    def search(self, query):
        query_words = query.lower().split()
        results = []

        for doc in self.documents:

            if not self.metadata.is_approved(doc["name"]):
                continue

            score = sum(
                word in doc["content"].lower()
                for word in query_words
            )

            if score:
                results.append({
                    "source": doc["name"],
                    "score": score,
                    "content": doc["content"]
                })

        return sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )

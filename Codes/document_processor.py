from utils import read_documents


class DocumentProcessor:

    def __init__(self, folder):
        self.documents = read_documents(folder)

    def process(self):
        return self.documents

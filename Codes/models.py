from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Source:
    name: str
    path: str
    department: str
    approval_status: str = "Approved"
    confidentiality: str = "Internal"


@dataclass
class Document:
    source: Source
    content: str


@dataclass
class Answer:
    response: str
    citations: List[str]
    status: str = "Complete"

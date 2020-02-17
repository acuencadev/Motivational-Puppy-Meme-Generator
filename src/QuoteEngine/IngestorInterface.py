from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    accepted_extensions = []
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        extension = path.split('.')[-1]
        
        return extension in cls.accepted_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

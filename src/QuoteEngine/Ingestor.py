from typing import List

from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .QuoteModel import QuoteModel


class Ingestor:
    ingestors: List[IngestorInterface] = [CSVIngestor]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        
        raise Exception("Could not find a parser for the selected file.")

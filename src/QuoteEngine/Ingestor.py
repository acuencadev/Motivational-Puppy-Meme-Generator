from typing import List

from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor


class Ingestor:
    ingestors: List[IngestorInterface] = [
        CSVIngestor,
        DocxIngestor,
        PDFIngestor,
        TXTIngestor
    ]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        
        raise Exception(f"Could not find a parser for the selected file: {path}")

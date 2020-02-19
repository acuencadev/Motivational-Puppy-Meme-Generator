from typing import List

from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor


class Ingestor:
    """
    Strategy object. Takes a list of ingestors and pick the most adequate
    to complete the task.
    """
    ingestors: List[IngestorInterface] = [
        CSVIngestor,
        DocxIngestor,
        PDFIngestor,
        TXTIngestor
    ]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Iterate over the list of registered ingestors and check if it can parse
        them.
        
        :param path: Path to the file to be processed.
        :return: List of Quotes extracted from the file.
        :raises Exception: If no ingestor is found to process the file.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        
        raise Exception(f"Could not find a parser for the selected file: {path}")

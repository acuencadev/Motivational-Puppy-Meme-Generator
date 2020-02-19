from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """ Ingestor base abstract class. """
    
    allowed_extensions = []
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file can be parsed
        
        :param path: Path of the file.
        :return: Whether or not the file can be parsed.
        """
        
        extension = path.split('.')[-1]
        
        return extension in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a file.
        
        :param path: Path of the file.
        :return: List of Quotes extracted from the file.
        """
        
        pass

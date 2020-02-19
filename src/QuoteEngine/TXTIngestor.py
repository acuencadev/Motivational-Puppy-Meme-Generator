from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """ Process TXT files """
    
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a TXT file
        
        :param path: Path of the TXT file.
        :return: List of Quotes extracted from the TXT.
        """
        
        if not cls.can_ingest(path):
            raise Exception("Could not parse the selected file.")
        
        quotes = []
        
        with open(path, 'r', encoding='UTF-8') as fin:
            for line in fin.readlines():
                line = line.strip().split(' - ')
                quote = QuoteModel(body=line[0], author=line[1])
                quotes.append(quote)

        return quotes

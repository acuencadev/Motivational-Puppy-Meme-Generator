from typing import List

import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """ Process CSV files """
    
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a CSV file
        
        :param path: Path of the CSV file.
        :return: List of Quotes extracted from the CSV.
        """
        if not cls.can_ingest(path):
            raise Exception("Could not parse the selected file.")
        
        quotes = []
        df = pd.read_csv(path, header=0, delimiter=',')
        
        for _, row in df.iterrows():
            quote = QuoteModel(body=row['body'], author=row['author'])
            quotes.append(quote)
            
        return quotes

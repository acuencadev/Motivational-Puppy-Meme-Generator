from typing import List

import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Could not parse the selected file.")
        
        quotes = []
        df = pd.read_csv(path, header=0)
        
        for _, row in df.iterrows():
            quote = QuoteModel(body=df['body'], author=df['author'])
            quotes.append(quote)
            
        return quotes

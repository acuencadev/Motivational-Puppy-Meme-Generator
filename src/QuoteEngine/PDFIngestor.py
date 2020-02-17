import os
import subprocess
from random import randint
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Could not parse the selected file.")
        
        quotes = []
        
        tmp = f"./tmp/{randint(0, 100000000)}.txt"
        call = subprocess.call(['pdftotext', path, tmp])
        
        with open(tmp, 'r') as fin:
            for line in fin.readlines():
                line - line.strip('\n\r').strip()
                
                if len(line) > 0:
                    parse = line.split(' - ')
                    quote = QuoteModel(body=parse[0], author=parse[1])
                    quotes.append(quote)
        
        return quotes

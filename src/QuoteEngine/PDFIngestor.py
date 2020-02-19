import os
import subprocess
from typing import List
from uuid import uuid4

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """ Process PDF files """
    
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a PDF file
        
        :param path: Path of the PDF file.
        :return: List of Quotes extracted from the PDF.
        """
        
        if not cls.can_ingest(path):
            raise Exception("Could not parse the selected file.")
                
        quotes = []
        
        tmp = f"./tmp/{uuid4()}.txt"
        
        call = subprocess.call(['pdftotext',
                                path,
                                tmp])
        
        with open(tmp, 'r') as fin:
            for line in fin.readlines():
                line = line.strip('\n\r').strip()
                
                if len(line) > 0:
                    parse = line.split(' - ')
                    quote = QuoteModel(body=parse[0], author=parse[1])
                    quotes.append(quote)
                    
        os.remove(tmp)
        
        return quotes

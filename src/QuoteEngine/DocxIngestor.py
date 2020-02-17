from typing import List

from docx import Document

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['doc', 'docx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Could not parse the selected file.")
        
        quotes = []
        doc = Document(path)
        
        for para in doc.paragraphs:
            parse = para.text.strip().split(' - ')
            
            if len(parse) > 1:                
                quote = QuoteModel(body=parse[0], author=parse[1])
                quotes.append(quote)
            
        return quotes

class QuoteModel:
    """ Simple POPO Object to represent a Quote """
    
    __slots__ = ['body', 'author']

    def __init__(self, body: str, author: str):
        """
        Initialize the QuoteModel object.
        
        :param body: Body of the quote.
        :param author: Author of the quote.
        :return: None
        """
        
        self.body = body
        self.author = author
        
    def __repr__(self):
        """ String representation of the object """
        return f"{self.body} - {self.author}"

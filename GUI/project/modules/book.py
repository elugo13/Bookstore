class Book:

    def __init__(self, book_info: dict) -> None:
        self.id = book_info['id']
        self.name = book_info['name']
        self.description = book_info['description']
        self.isbn = book_info['isbn']
        self.page_count = book_info['page_count']
        self.issued = book_info['issued']
        self.author = book_info['author']
        self.year = book_info['year']

    def to_dict(self) -> dict:
        dictionary = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "isbn": self.isbn,
            "page_count": self.page_count,
            "issued": self.issued,
            "author": self.author,
            "year": self.year
        }
        return dictionary

class Book:

    def __init__(self, id: int, name: str, description: str, isbn: str,
                 page_count: int, issued: bool, author: str, year: int) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.isbn = isbn
        self.page_count = page_count
        self.issued = issued
        self.author = author
        self.year = year

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

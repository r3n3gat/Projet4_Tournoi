from models.book import Book

# Création d'un objet Book
book_test = Book(
    title="Harry Potter à l'école des sorciers",
    price="12.99€",
    stock=True,
    rating=5,
    category="Fantasy",
    image_url="https://example.com/harry_potter.jpg"
)

# Affichage du livre
print(book_test)

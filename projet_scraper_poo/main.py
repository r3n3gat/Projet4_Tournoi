from models.book import Book
from models.category import Category

# Création d'une catégorie
fantasy = Category("Fantasy")

# Création de quelques livres
book1 = Book(
    title="Harry Potter à l'école des sorciers",
    price="12.99€",
    stock=True,
    rating=5,
    category="Fantasy",
    image_url="https://example.com/harry_potter.jpg"
)

book2 = Book(
    title="Le Seigneur des Anneaux",
    price="15.50€",
    stock=True,
    rating=5,
    category="Fantasy",
    image_url="https://example.com/lotr.jpg"
)

# Ajout des livres dans la catégorie
fantasy.add_book(book1)
fantasy.add_book(book2)

# Affichage de la catégorie et de ses livres
print(fantasy)
for book in fantasy.books:
    print(book)

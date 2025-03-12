from models.book import Book
from models.category import Category
from models.data_manager import DataManager

# Création d'une catégorie et de livres
fantasy = Category("Fantasy")

book1 = Book("Harry Potter", "12.99€", True, 5, "Fantasy", "https://example.com/harry.jpg")
book2 = Book("Le Seigneur des Anneaux", "15.50€", True, 5, "Fantasy", "https://example.com/lotr.jpg")

# Ajout des livres à la catégorie
fantasy.add_book(book1)
fantasy.add_book(book2)

# Création du gestionnaire de données
data_manager = DataManager()

# Sauvegarde des livres
data_manager.save_books_to_csv(fantasy.books, "fantasy_books.csv")
data_manager.save_books_to_json(fantasy.books, "fantasy_books.json")

# Chargement des livres
loaded_books = data_manager.load_books_from_json("fantasy_books.json")

# Affichage des livres chargés
print("\nLivres chargés depuis JSON :")
for book in loaded_books:
    print(book)

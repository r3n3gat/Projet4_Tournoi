import csv
import json
import os


class DataManager:
    """
    Classe gérant la sauvegarde et le chargement des livres et catégories dans des fichiers CSV et JSON.
    """

    def __init__(self, data_folder="data"):
        """
        Initialise le gestionnaire de données.

        :param data_folder: Dossier où stocker les fichiers de données.
        """
        self.data_folder = data_folder
        os.makedirs(self.data_folder, exist_ok=True)  # Crée le dossier s'il n'existe pas

    def save_books_to_csv(self, books, filename="books.csv"):
        """
        Sauvegarde une liste de livres dans un fichier CSV.

        :param books: Liste d'objets Book
        :param filename: Nom du fichier CSV
        """
        filepath = os.path.join(self.data_folder, filename)
        with open(filepath, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Stock", "Rating", "Category", "Image URL"])
            for book in books:
                writer.writerow([book.title, book.price, book.stock, book.rating, book.category, book.image_url])

        print(f"[INFO] Livres sauvegardés dans {filepath}")

    def save_books_to_json(self, books, filename="books.json"):
        """
        Sauvegarde une liste de livres dans un fichier JSON.

        :param books: Liste d'objets Book
        :param filename: Nom du fichier JSON
        """
        filepath = os.path.join(self.data_folder, filename)
        books_data = [book.__dict__ for book in books]
        with open(filepath, mode="w", encoding="utf-8") as file:
            json.dump(books_data, file, indent=4, ensure_ascii=False)

        print(f"[INFO] Livres sauvegardés dans {filepath}")

    def load_books_from_json(self, filename="books.json"):
        """
        Charge une liste de livres depuis un fichier JSON.

        :param filename: Nom du fichier JSON
        :return: Liste d'objets Book
        """
        filepath = os.path.join(self.data_folder, filename)
        if not os.path.exists(filepath):
            print(f"[WARN] Fichier {filepath} introuvable.")
            return []

        with open(filepath, mode="r", encoding="utf-8") as file:
            books_data = json.load(file)

        from models.book import Book  # Importation ici pour éviter les références circulaires
        books = [Book(**data) for data in books_data]

        print(f"[INFO] {len(books)} livres chargés depuis {filepath}")
        return books

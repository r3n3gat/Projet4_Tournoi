class Category:
    """
    Modèle représentant une catégorie de livres.
    """

    def __init__(self, name):
        """
        Initialise une catégorie avec un nom et une liste de livres.

        :param name: Nom de la catégorie
        """
        self.name = name
        self.books = []  # Liste des livres dans cette catégorie

    def add_book(self, book):
        """
        Ajoute un livre à la catégorie.

        :param book: Objet Book à ajouter
        """
        self.books.append(book)

    def __str__(self):
        """
        Retourne une représentation textuelle de la catégorie et des livres qu'elle contient.
        """
        return f"Catégorie : {self.name} - {len(self.books)} livres"

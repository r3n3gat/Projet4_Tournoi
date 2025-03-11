class Book:
    """
    Modèle représentant un livre extrait du site Books to Scrape.
    """

    def __init__(self, title, price, stock, rating, category, image_url):
        """
        Initialise un objet Book avec ses attributs.

        :param title: Titre du livre
        :param price: Prix du livre
        :param stock: Disponibilité du livre (en stock ou non)
        :param rating: Note du livre (1 à 5 étoiles)
        :param category: Catégorie du livre
        :param image_url: URL de l'image du livre
        """
        self.title = title
        self.price = price
        self.stock = stock
        self.rating = rating
        self.category = category
        self.image_url = image_url

    def __str__(self):
        """
        Retourne une représentation textuelle du livre.
        """
        return f"{self.title} - {self.price} - Stock: {self.stock} - Note: {self.rating}★ - Catégorie: {self.category}"

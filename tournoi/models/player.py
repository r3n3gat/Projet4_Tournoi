class Player:
    """Modèle représentant un joueur d'échecs."""

    def __init__(self, last_name, first_name, birth_date, chess_id, score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id  # Identifiant unique
        self.score = score  # Score cumulé dans le tournoi

    def __repr__(self):
        return f"<Player {self.first_name} {self.last_name} - ID: {self.chess_id} - Score: {self.score}>"

    @property
    def id(self):
        """Alias pratique pour l'identifiant d'échecs."""
        return self.chess_id

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour JSON."""
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un objet Player à partir d'un dictionnaire JSON."""
        return cls(**data)


if __name__ == "__main__":
    print("\n[INFO] ✅ Test de la classe Player")
    player = Player("Enoto", "Stevi", "30-07-1977", "FR12345")
    print(player)
    print(player.to_dict())

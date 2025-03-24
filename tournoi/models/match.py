from .player import Player   # Import de la classe Player

class Match:
    """Modèle représentant un match entre deux joueurs."""

    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def __repr__(self):
        return f"<Match {self.player1.first_name} vs {self.player2.first_name} - Score: {self.score1} - {self.score2}>"

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour JSON."""
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "score1": self.score1,
            "score2": self.score2
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un objet Match à partir d'un dictionnaire (JSON)."""
        player1 = Player.from_dict(data["player1"])
        player2 = Player.from_dict(data["player2"])
        return cls(player1, player2, data["score1"], data["score2"])

if __name__ == "__main__":
    p1 = Player("Enoto", "Stevi", "30-07-1977", "fr12345")
    p2 = Player("Mentor", "Fred", "01-001-1997", "fr11223")
    p3 = Player("Dupond", "Robert", "30-07-1979", "fr123456")
    p4 = Player("Menton", "Fab", "01-001-1997", "fr112233")

    match = Match(p1, p2, 1, 0)
    print(match)
    print(match.to_dict())


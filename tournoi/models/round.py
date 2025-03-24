from .player import Player   # Import de la classe Player
from .match import Match   # Import de la classe Match
class Round:
    """Modèle représentant un tour d'un tournoi."""

    def __init__(self, name, matches=[], start_date=None, end_date=None):
        self.name = name
        self.matches = matches
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Round {self.name} - {len(self.matches)} matchs>"

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour JSON."""
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_date": self.start_date,
            "end_date": self.end_date
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un objet Round à partir d'un dictionnaire (JSON)."""
        matches = [Match.from_dict(m) for m in data["matches"]]
        return cls(data["name"], matches, data["start_date"], data["end_date"])


if __name__ == "__main__":
    p1 = Player("Enoto", "Stevi", "30-07-1977", "fr12345")
    p2 = Player("Mentor", "Fred", "01-001-1997", "fr11223")
    p3 = Player("Dupond", "Robert", "30-07-1979", "fr123456")
    p4 = Player("Menton", "Fab", "01-001-1997", "fr112233")

    match = Match(p1, p2, 1, 0)

    # Création d'un round normalement
    round1 = Round("Round 1", [match])
    print(round1)
    print(round1.to_dict())

    # Simulation de sauvegarde en JSON puis rechargement avec from_dict()
    round_data = round1.to_dict()  # On simule une sauvegarde
    round_reloaded = Round.from_dict(round_data)  # On recharge depuis le JSON
    print("\n[INFO] Round rechargé depuis JSON :")
    print(round_reloaded)


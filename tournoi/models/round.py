from datetime import datetime
import random
from .match import Match


class Round:
    """Modèle représentant un round dans un tournoi."""

    def __init__(self, nom, matchs=None, start_date=None, end_date=None):
        self.nom = nom
        self.start_date = start_date or str(datetime.now())
        self.end_date = end_date
        self.matchs = matchs if matchs else []

    def __repr__(self):
        return f"<Round {self.nom} - {len(self.matchs)} matchs>"

    def close_round(self):
        """Marque la fin du round."""
        self.end_date = str(datetime.now())

    def to_dict(self):
        """Convertit le round en dictionnaire JSON-sérialisable."""
        return {
            "nom": self.nom,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matchs": [match.to_dict() for match in self.matchs]
        }

    @classmethod
    def from_dict(cls, data):
        from .match import Match
        matchs = [Match.from_dict(m) for m in data.get("matchs", [])]
        return cls(
            nom=data.get("nom", "Round inconnu"),
            start_date=data.get("start_date", ""),
            end_date=data.get("end_date", ""),
            matchs=matchs
        )

    @staticmethod
    def generate_pairs(players, previous_matches=None):
        """
        Génère des paires de joueurs :
        - 1er round : aléatoire
        - Sinon : classement par score
        - Évite les doublons si previous_matches fourni (liste de tuples de IDs)
        """
        if not players:
            print("[ERREUR] Aucun joueur fourni pour l’appariement.")
            return []

        previous_matches = previous_matches or []
        pairs = []

        # Tri par score décroissant
        players_sorted = sorted(players, key=lambda p: p.score, reverse=True)
        used = set()

        for i in range(len(players_sorted)):
            if i in used:
                continue
            p1 = players_sorted[i]
            for j in range(i + 1, len(players_sorted)):
                if j in used:
                    continue
                p2 = players_sorted[j]
                if (p1.id, p2.id) not in previous_matches and (p2.id, p1.id) not in previous_matches:
                    pairs.append((p1, p2))
                    used.update([i, j])
                    break

        # Si on ne peut pas générer assez de paires sans doublon
        if len(pairs) < len(players) // 2:
            print("[⚠️] Tous les joueurs se sont déjà affrontés.")
            print("[INFO] Appariement aléatoire activé pour compléter le round.")
            random.shuffle(players)
            pairs = [(players[i], players[i + 1]) for i in range(0, len(players) - 1, 2)]

        return pairs

    @classmethod
    def create_round(cls, nom, players, previous_matches=None):
        """Crée un round complet avec les paires générées et les matchs associés."""
        pairs = cls.generate_pairs(players, previous_matches)
        matchs = [Match(p1, p2) for p1, p2 in pairs]
        return cls(nom=nom, matchs=matchs)

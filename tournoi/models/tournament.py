from .round import Round
from .player import Player


class Tournament:
    """Modèle représentant un tournoi d'échecs."""

    def __init__(self, nom, lieu, date_debut, date_fin,
                 joueurs=None, rounds=None, remarques=""):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.joueurs = joueurs if joueurs else []
        self.rounds = rounds if rounds else []
        self.remarques = remarques

    def __repr__(self):
        return f"<Tournoi {self.nom} - {len(self.joueurs)} joueurs - {len(self.rounds)} rounds>"

    def to_dict(self):
        """Convertit l'objet en dictionnaire sérialisable JSON."""
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "joueurs": [joueur.to_dict() for joueur in self.joueurs],
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "remarques": self.remarques
        }

    @classmethod
    def from_dict(cls, data):
        """Recrée un tournoi depuis un dictionnaire JSON."""
        joueurs_data = data.get("joueurs", data.get("players", []))
        joueurs = [Player.from_dict(p) for p in joueurs_data]
        rounds = [Round.from_dict(r) for r in data.get("rounds", [])]

        return cls(
            nom=data.get("nom", data.get("name", "Tournoi sans nom")),
            lieu=data.get("lieu", data.get("location", "Lieu inconnu")),
            date_debut=data.get("date_debut", data.get("start_date", "")),
            date_fin=data.get("date_fin", data.get("end_date", "")),
            joueurs=joueurs,
            rounds=rounds,
            remarques=data.get("remarques", "")
        )

    def add_round(self, round_):
        """Ajoute un round au tournoi."""
        self.rounds.append(round_)

    def start_new_round(self):
        """Crée un nouveau round avec appariement."""
        if len(self.rounds) >= 4:
            print("[INFO] Le tournoi a déjà 4 rounds. Terminé.")
            return None

        nom_round = f"Round {len(self.rounds) + 1}"

        previous_matches = [
            (match.player1.id, match.player2.id)
            for round_ in self.rounds
            for match in round_.matchs
        ]

        nouveau_round = Round.create_round(nom_round, self.joueurs, previous_matches)
        self.add_round(nouveau_round)

        print(f"[INFO] Nouveau round généré : {nom_round}")
        return nouveau_round

    def get_classement(self):
        """Reconstruit le classement des joueurs depuis les rounds."""
        classement = {}

        for round_ in self.rounds:
            for match in round_.matchs:
                for joueur, score in [(match.player1, match.score1), (match.player2, match.score2)]:
                    if joueur.chess_id not in classement:
                        classement[joueur.chess_id] = joueur
                        classement[joueur.chess_id].score = 0
                    classement[joueur.chess_id].score += score

        return sorted(classement.values(), key=lambda j: j.score, reverse=True)

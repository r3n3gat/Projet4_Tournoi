import json
import os
import random
from datetime import datetime
from .round import Round
from .player import Player
from .match import Match  #  Import ajouté pour créer des matchs


class Tournament:
    """Modèle représentant un tournoi d'échecs."""

    def __init__(self, name, location, start_date, end_date, players=None, rounds=None, notes=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players if players else []  # Liste de joueurs
        self.rounds = rounds if rounds else []  # Liste des tours
        self.notes = notes  # Remarques

    def __repr__(self):
        return f"<Tournament {self.name} - {len(self.players)} joueurs - {len(self.rounds)} rounds>"

    def to_dict(self):
        """Convertit le tournoi en dictionnaire pour JSON."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "players": [player.to_dict() for player in self.players],
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un tournoi à partir d'un dictionnaire JSON."""
        players = [Player.from_dict(p) for p in data["players"]]
        rounds = [Round.from_dict(r) for r in data["rounds"]]
        return cls(data["name"], data["location"], data["start_date"], data["end_date"], players, rounds, data["notes"])

    def add_player(self, player_obj):
        """Ajoute un joueur au tournoi."""
        self.players.append(player_obj)

    def add_round(self, round_obj):
        """Ajoute un tour au tournoi."""
        self.rounds.append(round_obj)

    def save_to_json(self, filename="tournaments.json"):
        """Sauvegarde le tournoi dans un fichier JSON."""
        filepath = os.path.join("data", filename)
        os.makedirs("data", exist_ok=True)

        # Charger les anciens tournois
        existing_tournaments = []
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                try:
                    existing_tournaments = json.load(file)
                except json.JSONDecodeError:
                    pass  # Fichier vide ou corrompu

        # Vérifier si le tournoi existe déjà
        existing_tournaments = [t for t in existing_tournaments if t["name"] != self.name]
        existing_tournaments.append(self.to_dict())

        # Sauvegarder la liste mise à jour
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(existing_tournaments, file, indent=4, ensure_ascii=False)

        print(f"[INFO]  Tournoi '{self.name}' sauvegardé dans {filepath}")

    @classmethod
    def load_from_json(cls, filename="tournaments.json"):
        """Charge la liste des tournois enregistrés."""
        filepath = os.path.join("data", filename)

        if not os.path.exists(filepath):
            print(f"[WARN]  Aucun fichier trouvé : {filepath}")
            return []

        with open(filepath, "r", encoding="utf-8") as file:
            try:
                tournaments_data = json.load(file)
                return [cls.from_dict(data) for data in tournaments_data]
            except json.JSONDecodeError:
                print(f"[ERREUR]  Fichier JSON corrompu : {filepath}")
                return []

    def generate_pairs(self):
        """Génère les paires de joueurs pour le prochain round."""
        if not self.players:
            print("[ERREUR] Aucun joueur enregistré dans ce tournoi.")
            return []

        print("[INFO]  Génération des paires de joueurs...")

        if len(self.rounds) == 0:
            # Premier round : appariement aléatoire
            players = self.players[:]
            random.shuffle(players)
        else:
            # Rounds suivants : classement par score
            players = sorted(self.players, key=lambda x: x.score, reverse=True)

        # Générer les paires de joueurs
        pairs = []
        for i in range(0, len(players) - 1, 2):
            p1, p2 = players[i], players[i + 1]
            pairs.append((p1, p2))

        if not pairs:
            print("[ERREUR] Impossible de générer des paires, pas assez de joueurs.")

        return pairs

    def start_new_round(self):
        """Démarre un nouveau round avec des paires de joueurs."""
        if len(self.rounds) >= 4:  # ⚠ Tournoi limité à 4 rounds
            print("[WARN]  Le tournoi a déjà 4 rounds. Impossible d'en ajouter un autre.")
            return None

        round_number = len(self.rounds) + 1
        round_name = f"Round {round_number}"

        #  Génération des paires pour ce round
        pairs = self.generate_pairs()
        matches = [Match(p1, p2) for p1, p2 in pairs]

        #  Création et ajout du round
        new_round = Round(round_name, matches, start_date=str(datetime.now()))
        self.rounds.append(new_round)

        print(f"[INFO]  Nouveau round ajouté : {round_name}")
        return new_round


if __name__ == "__main__":
    # Charger le tournoi existant
    loaded_tournaments = Tournament.load_from_json()
    tournament = loaded_tournaments[0] if loaded_tournaments else None

    if tournament:
        print("\n[INFO]  Génération des paires de joueurs...")
        pairs = tournament.generate_pairs()
        if pairs:
            for p1, p2 in pairs:
                print(f" - {p1.last_name} vs {p2.last_name}")

        # Démarrer un round et sauvegarder
        new_round = tournament.start_new_round()
        if new_round:
            tournament.save_to_json()
            print(f"[INFO]  Nouveau round ajouté : {new_round.name}")

    else:
        print("[ERREUR] Aucun tournoi trouvé.")

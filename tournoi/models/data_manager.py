import json
import os
from models.player import Player
from models.tournament import Tournament


class DataManager:
    """Gère la sauvegarde et le chargement des données JSON."""

    def __init__(self, data_folder="data"):
        self.data_folder = data_folder
        os.makedirs(data_folder, exist_ok=True)
        self.players_file = os.path.join(data_folder, "players.json")
        self.tournaments_file = os.path.join(data_folder, "tournaments.json")

    # ──────────────── Gestion des Joueurs ────────────────
    def save_players(self, players):
        """Sauvegarde une liste de joueurs dans players.json."""
        with open(self.players_file, "w", encoding="utf-8") as file:
            json.dump([p.to_dict() for p in players], file, indent=4, ensure_ascii=False)

    def load_players(self):
        """Charge la liste des joueurs depuis players.json."""
        if not os.path.exists(self.players_file):
            return []

        try:
            with open(self.players_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Player.from_dict(p) for p in data]
        except json.JSONDecodeError:
            print(" Fichier JSON corrompu : players.json")
            return []

    def add_player(self, player):
        """Ajoute un joueur s’il n’existe pas déjà (par ID)."""
        players = self.load_players()
        if any(p.chess_id == player.chess_id for p in players):
            return False
        players.append(player)
        self.save_players(players)
        print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès.")
        return True

    # ──────────────── Gestion des Tournois ────────────────
    def save_tournaments(self, tournaments):
        """Sauvegarde une liste de tournois dans tournaments.json."""
        with open(self.tournaments_file, "w", encoding="utf-8") as file:
            json.dump(
                [t.to_dict() for t in tournaments],
                file, indent=4, ensure_ascii=False)

    def load_tournaments(self):
        """Charge la liste des tournois depuis tournaments.json."""
        if not os.path.exists(self.tournaments_file):
            return []

        try:
            with open(self.tournaments_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Tournament.from_dict(t) for t in data]
        except json.JSONDecodeError:
            print("Fichier JSON corrompu : tournaments.json")
            return []

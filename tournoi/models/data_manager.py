import json
import os


class DataManager:
    """Gère la sauvegarde et le chargement des données en JSON pour joueurs et tournois."""

    def __init__(self, data_folder="data"):
        self.data_folder = data_folder
        os.makedirs(self.data_folder, exist_ok=True)
        self.players_file = os.path.join(self.data_folder, "players.json")
        self.tournaments_file = os.path.join(self.data_folder, "tournaments.json")

    # 🔹 Gestion des joueurs
    def save_players(self, players):
        from .player import Player
        with open(self.players_file, "w", encoding="utf-8") as file:
            json.dump([player.to_dict() for player in players], file, indent=4, ensure_ascii=False)
        print(f"[INFO] 📂 Joueurs sauvegardés dans {self.players_file}")

    def load_players(self):
        from .player import Player
        if not os.path.exists(self.players_file):
            print(f"[WARN] Aucun fichier trouvé : {self.players_file}")
            return []
        with open(self.players_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return [Player.from_dict(p) for p in data]
            except json.JSONDecodeError:
                print(f"[ERREUR] Fichier JSON corrompu : {self.players_file}")
                return []

    def add_player(self, player):
        players = self.load_players()
        if any(p.chess_id == player.chess_id for p in players):
            print(f"[⛔] Un joueur avec l’ID {player.chess_id} existe déjà.")
            return False
        players.append(player)
        self.save_players(players)
        print(f"[✅] Joueur {player.first_name} {player.last_name} ajouté avec succès.")
        return True

    # 🔹 Gestion des tournois
    def save_tournaments(self, tournaments):
        from .tournament import Tournament
        with open(self.tournaments_file, "w", encoding="utf-8") as file:
            json.dump([t.to_dict() for t in tournaments], file, indent=4, ensure_ascii=False)
        print(f"[INFO] 📂 Tournois sauvegardés dans {self.tournaments_file}")

    def load_tournaments(self):
        from .tournament import Tournament
        if not os.path.exists(self.tournaments_file):
            print(f"[WARN] Aucun fichier trouvé : {self.tournaments_file}")
            return []
        with open(self.tournaments_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return [Tournament.from_dict(t) for t in data]
            except json.JSONDecodeError:
                print(f"[ERREUR] Fichier JSON corrompu : {self.tournaments_file}")
                return []

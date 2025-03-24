import json
import os


class DataManager:
    """Gère la sauvegarde et le chargement des données en JSON pour joueurs et tournois."""

    def __init__(self, data_folder="data"):
        self.data_folder = data_folder
        os.makedirs(self.data_folder, exist_ok=True)  # 📂 Crée le dossier si besoin
        self.players_file = os.path.join(self.data_folder, "players.json")
        self.tournaments_file = os.path.join(self.data_folder, "tournaments.json")

    # ✅ Gestion des joueurs
    def save_players(self, players):
        """💾 Sauvegarde une liste de joueurs dans players.json"""
        with open(self.players_file, "w", encoding="utf-8") as file:
            json.dump([player.to_dict() for player in players], file, indent=4, ensure_ascii=False)
        print(f"[INFO] 📂 Joueurs sauvegardés dans {self.players_file}")

    def load_players(self):
        """📂 Charge les joueurs depuis players.json"""
        from models.player import Player  # ✅ Import différé pour éviter le problème circulaire

        if not os.path.exists(self.players_file):
            print(f"[WARN] 📂 Aucun fichier trouvé : {self.players_file}")
            return []

        with open(self.players_file, "r", encoding="utf-8") as file:
            try:
                players_data = json.load(file)
                return [Player.from_dict(data) for data in players_data]
            except json.JSONDecodeError:
                print(f"[ERREUR] 📂 Fichier JSON corrompu : {self.players_file}")
                return []

    # ✅ Gestion des tournois
    def save_tournaments(self, tournaments):
        """💾 Sauvegarde une liste de tournois dans tournaments.json"""
        with open(self.tournaments_file, "w", encoding="utf-8") as file:
            json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4, ensure_ascii=False)
        print(f"[INFO] 📂 Tournois sauvegardés dans {self.tournaments_file}")

    def load_tournaments(self):
        """📂 Charge les tournois depuis tournaments.json"""
        from models.tournament import Tournament  # ✅ Import différé pour éviter le problème circulaire

        if not os.path.exists(self.tournaments_file):
            print(f"[WARN] 📂 Aucun fichier trouvé : {self.tournaments_file}")
            return []

        with open(self.tournaments_file, "r", encoding="utf-8") as file:
            try:
                tournaments_data = json.load(file)
                return [Tournament.from_dict(data) for data in tournaments_data]
            except json.JSONDecodeError:
                print(f"[ERREUR] 📂 Fichier JSON corrompu : {self.tournaments_file}")
                return []


if __name__ == "__main__":
    from models.player import Player  # ✅ Import uniquement pour les tests

    manager = DataManager()

    # 🔹 Création de joueurs test
    p1 = Player("Enoto", "Stevi", "30-07-1977", "fr12345")
    p2 = Player("Mentor", "Fred", "01-01-1997", "fr11223")
    p3 = Player("Dupond", "Robert", "30-07-1979", "fr123456")
    p4 = Player("Menton", "Fab", "01-01-1997", "fr112233")

    players = [p1, p2, p3, p4]

    # 🔽 Sauvegarde et Chargement des joueurs
    manager.save_players(players)
    loaded_players = manager.load_players()
    print("\n[INFO] 📂 Joueurs chargés depuis JSON :")
    for player in loaded_players:
        print(player)

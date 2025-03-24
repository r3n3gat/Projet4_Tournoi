from models.tournament import Tournament
from models.player import Player

# Création d'un tournoi
tournament = Tournament("Championnat Local", "Paris", "2025-06-01", "2025-06-05")

# Ajout des joueurs
tournament.add_player(Player("Enoto", "Stevi", "30-07-1977", "fr12345"))
tournament.add_player(Player("Mentor", "Fred", "01-01-1997", "fr11223"))
tournament.add_player(Player("Dupond", "Robert", "30-07-1979", "fr123456"))
tournament.add_player(Player("Menton", "Fab", "01-02-1990", "fr112233"))

# Sauvegarde dans JSON
tournament.save_to_json()
print("[INFO] Tournoi créé et sauvegardé !")

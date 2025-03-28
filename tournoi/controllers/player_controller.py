from models.player import Player
from models.data_manager import DataManager
from views import display


class PlayerController:
    """🎮 Contrôleur pour gérer les opérations liées aux joueurs."""

    def __init__(self):
        self.data_manager = DataManager()

    def display_menu(self):
        while True:
            print("\n=== GESTION DES JOUEURS ===")
            print("1. Ajouter un joueur")
            print("2. Lister les joueurs")
            print("3. Retour")

            choice = input("Choisissez une option (1-3) : ")

            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.list_players()
            elif choice == "3":
                display.message_info("Retour au menu principal.")
                break
            else:
                display.message_erreur("Entrée invalide. Veuillez recommencer.")

    def add_player(self):
        print("\n=== AJOUTER UN JOUEUR ===")
        last_name = input("Nom : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (jj-mm-aaaa) : ")
        chess_id = input("Identifiant national (ex : AB12345) : ")

        new_player = Player(last_name, first_name, birth_date, chess_id)
        success = self.data_manager.add_player(new_player)

        if success:
            display.message_succes(f"Joueur {first_name} {last_name} ajouté.")
        else:
            display.message_erreur("Échec : identifiant déjà utilisé.")

    def list_players(self):
        joueurs = self.data_manager.load_players()
        display.afficher_liste_joueurs(joueurs)

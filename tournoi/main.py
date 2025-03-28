from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


def main():
    """Point d’entrée principal du gestionnaire de tournois."""
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Gérer les joueurs")
        print("2.  Gérer les tournois")
        print("3. Quitter")

        choix = input("Choisissez une option (1-3) : ")

        if choix == "1":
            player_controller.display_menu()
        elif choix == "2":
            tournament_controller.display_menu()
        elif choix == "3":
            print("\n Merci d’avoir utilisé le gestionnaire de tournois ! À bientôt.")
            break
        else:
            print("\n Entrée invalide. Veuillez choisir 1, 2 ou 3.")


if __name__ == "__main__":
    main()

from models.tournament import Tournament
from models.data_manager import DataManager
from views import display
from utils.html_exporter import export_tournament_to_html
from utils.markdown_exporter import export_tournament_to_markdown


class TournamentController:
    """♟️ Contrôleur principal pour gérer les tournois."""

    def __init__(self):
        self.data_manager = DataManager()

    def display_menu(self):
        while True:
            print("\n=== GESTION DES TOURNOIS ===")
            print("1.  Créer un tournoi")
            print("2.  Lister les tournois")
            print("3.  Continuer un tournoi")
            print("4.  Retour")
            print("5.  Créer un tournoi de test")
            print("6.  Exporter un tournoi en Markdown")

            action = input("Votre choix (1-6) : ")

            if action == "1":
                self.create_tournament()
            elif action == "2":
                self.list_tournaments()
            elif action == "3":
                self.continue_tournament()
            elif action == "4":
                display.message_info("Retour au menu principal.")
                break
            elif action == "5":
                self.create_test_tournament()
            elif action == "6":
                self.export_markdown()
            else:
                display.message_erreur("Choix invalide.")

    def create_tournament(self):
        print("\n=== ➕ CRÉER UN NOUVEAU TOURNOI ===")
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu : ")
        date_debut = input("Date de début (jj-mm-aaaa) : ")
        date_fin = input("Date de fin (jj-mm-aaaa) : ")
        remarques = input("Remarques éventuelles : ")

        all_players = self.data_manager.load_players()
        display.afficher_liste_joueurs(all_players)

        print("\nSélectionnez les joueurs du tournoi (min 2, max 8)")
        selections = input("Entrez les numéros séparés par des virgules : ")
        try:
            indices = [int(x.strip()) - 1 for x in selections.split(",")]
            joueurs = [
                all_players[i]
                for i in indices
                if 0 <= i < len(all_players)
            ]
        except ValueError:
            display.message_erreur("Format invalide.")
            return

        if len(joueurs) < 2:
            display.message_erreur("Minimum 2 joueurs requis.")
            return

        tournoi = Tournament(
            nom=nom,
            lieu=lieu,
            date_debut=date_debut,
            date_fin=date_fin,
            joueurs=joueurs,
            rounds=[],
            remarques=remarques
        )

        tournois = self.data_manager.load_tournaments()
        tournois.append(tournoi)
        self.data_manager.save_tournaments(tournois)

        display.message_succes(
            f"Tournoi '{nom}' créé avec {len(joueurs)} joueurs."
        )

    def list_tournaments(self):
        tournois = self.data_manager.load_tournaments()
        display.afficher_liste_tournois(tournois)

    def continue_tournament(self):
        tournois = self.data_manager.load_tournaments()
        if not tournois:
            display.message_erreur("Aucun tournoi existant.")
            return

        print("\n===  CONTINUER UN TOURNOI ===")
        for i, t in enumerate(tournois, 1):
            print(f"{i}. {t.nom} ({len(t.rounds)} rounds)")

        try:
            choix = int(input("Sélectionnez un tournoi : ")) - 1
            tournoi = tournois[choix]
        except (ValueError, IndexError):
            display.message_erreur("Sélection invalide.")
            return

        self.manage_tournament(tournoi)
        self.data_manager.save_tournaments(tournois)

    def manage_tournament(self, tournoi):
        while True:
            print(f"\n===  {tournoi.nom} ===")
            print("1.  Démarrer un nouveau round")
            print("2.  Saisir les résultats du round en cours")
            print("3.  Voir classement")
            print("4.  Retour")
            print("5.  Exporter le tournoi en HTML")

            choix = input("Choix : ")

            if choix == "1":
                round_ = tournoi.start_new_round()
                if round_:
                    display.message_succes(f"Round lancé : {round_.nom}")
            elif choix == "2":
                self.enter_results(tournoi)
            elif choix == "3":
                classement = tournoi.get_classement()
                display.afficher_classement(classement)
            elif choix == "4":
                display.message_info("Retour au menu précédent.")
                break
            elif choix == "5":
                export_tournament_to_html(tournoi)
            else:
                display.message_erreur("Choix invalide.")

    def enter_results(self, tournoi):
        if not tournoi.rounds:
            display.message_erreur("Aucun round à remplir.")
            return

        last_round = tournoi.rounds[-1]
        if last_round.end_date:
            display.message_info("Ce round est déjà terminé.")
            return

        print(f"[INFO] Résultats pour {last_round.nom}")
        for match in last_round.matchs:
            p1 = match.player1
            p2 = match.player2
            print(f"\nMatch : {p1.first_name} vs {p2.first_name}")
            while True:
                result = input("Résultat (1-0, 0.5-0.5, 0-1) : ")
                if result in ["1-0", "0.5-0.5", "0-1"]:
                    break
                display.message_erreur(
                    " Format invalide. Utilisez : 1-0, 0.5-0.5 ou 0-1."
                )

            if result == "1-0":
                match.score1, match.score2 = 1, 0
            elif result == "0.5-0.5":
                match.score1, match.score2 = 0.5, 0.5
            else:
                match.score1, match.score2 = 0, 1

            match.player1.score += match.score1
            match.player2.score += match.score2

        last_round.close_round()
        display.message_succes(f"Résultats enregistrés pour {last_round.nom}.")

    def create_test_tournament(self):
        from models.player import Player
        p1 = Player("Test", "Alice", "01/01/1990", "fr0001")
        p2 = Player("Test", "Bob", "02/02/1991", "fr0002")
        p3 = Player("Test", "Charlie", "03/03/1992", "fr0003")
        p4 = Player("Test", "Diana", "04/04/1993", "fr0004")

        tournoi = Tournament(
            nom="Tournoi Test",
            lieu="DevLand",
            date_debut="2025-04-01",
            date_fin="2025-04-03",
            joueurs=[p1, p2, p3, p4],
            remarques="Tournoi fictif pour les tests."
        )

        tournois = self.data_manager.load_tournaments()
        tournois.append(tournoi)
        self.data_manager.save_tournaments(tournois)

        display.message_succes("Tournoi de test créé avec 4 joueurs fictifs.")

    def export_markdown(self):
        tournois = self.data_manager.load_tournaments()
        if not tournois:
            display.message_erreur("Aucun tournoi à exporter.")
            return

        print("\n===  EXPORT MARKDOWN ===")
        for i, t in enumerate(tournois, 1):
            print(f"{i}. {t.nom}")

        try:
            choix = int(input("Quel tournoi exporter ? : ")) - 1
            tournoi = tournois[choix]
        except (ValueError, IndexError):
            display.message_erreur("Sélection invalide.")
            return

        export_tournament_to_markdown(tournoi)

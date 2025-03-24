from models.tournament import Tournament
from models.player import Player
from models.data_manager import DataManager
from views import display
from utils.html_exporter import export_tournament_to_html
from utils.markdown_exporter import export_tournament_to_markdown


class TournamentController:
    def __init__(self):
        self.data_manager = DataManager()

    def display_menu(self):
        while True:
            print("\n=== GESTION DES TOURNOIS ===")
            print("1. ➕ Créer un tournoi")
            print("2. 📋 Lister les tournois")
            print("3. 🧩 Continuer un tournoi")
            print("4. 🔙 Retour")
            print("5. 🧪 Créer un tournoi de test")
            print("6. 📄 Exporter un tournoi en Markdown")

            choix = input("Votre choix (1-6) : ")

            if choix == "1":
                self.create_tournament()
            elif choix == "2":
                self.list_tournaments()
            elif choix == "3":
                self.continue_tournament()
            elif choix == "4":
                display.message_info("Retour au menu principal.")
                break
            elif choix == "5":
                self.create_test_tournament()
            elif choix == "6":
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

        tournoi = Tournament(
            nom=nom,
            lieu=lieu,
            date_debut=date_debut,
            date_fin=date_fin,
            remarques=remarques
        )

        joueurs = self.data_manager.load_players()
        if len(joueurs) < 2:
            display.message_erreur("Pas assez de joueurs enregistrés.")
            return

        display.afficher_liste_joueurs(joueurs)

        print("\n🔽 Sélectionnez les joueurs du tournoi (min 2, max 8)")
        selection = input("Entrez les numéros séparés par des virgules : ")
        indexes = [int(i.strip()) - 1 for i in selection.split(",") if i.strip().isdigit()]

        for i in indexes:
            if 0 <= i < len(joueurs):
                tournoi.joueurs.append(joueurs[i])

        if len(tournoi.joueurs) < 2:
            display.message_erreur("Minimum 2 joueurs requis.")
            return

        tournois = self.data_manager.load_tournaments()
        tournois.append(tournoi)
        self.data_manager.save_tournaments(tournois)

        display.message_succes(f"Tournoi '{tournoi.nom}' créé avec {len(tournoi.joueurs)} joueurs.")

    def create_test_tournament(self):
        print("\n🧪 Création d’un tournoi de test...")

        p1 = Player("Test", "Alice", "01-01-1990", "TEST001")
        p2 = Player("Test", "Bob", "02-02-1990", "TEST002")
        p3 = Player("Test", "Charlie", "03-03-1990", "TEST003")
        p4 = Player("Test", "Diana", "04-04-1990", "TEST004")

        tournoi = Tournament(
            nom="Tournoi Test",
            lieu="DevLand",
            date_debut="2025-04-01",
            date_fin="2025-04-03",
            joueurs=[p1, p2, p3, p4],
            remarques="Tournoi fictif pour tests"
        )

        tournois = self.data_manager.load_tournaments()
        tournois.append(tournoi)
        self.data_manager.save_tournaments(tournois)

        display.message_succes("Tournoi de test créé avec 4 joueurs fictifs.")

    def list_tournaments(self):
        tournois = self.data_manager.load_tournaments()
        display.afficher_liste_tournois(tournois)

    def continue_tournament(self):
        tournois = self.data_manager.load_tournaments()
        if not tournois:
            display.message_erreur("Aucun tournoi disponible.")
            return

        print("\n=== 🧩 CONTINUER UN TOURNOI ===")
        for i, tournoi in enumerate(tournois, 1):
            print(f"{i}. {tournoi.nom} ({len(tournoi.rounds)} rounds)")

        choix = input("Sélectionnez un tournoi : ")
        if not choix.isdigit() or not (1 <= int(choix) <= len(tournois)):
            display.message_erreur("Choix invalide.")
            return

        tournoi = tournois[int(choix) - 1]

        while True:
            print(f"\n=== ⚙️ {tournoi.nom} ===")
            print("1. 🌀 Démarrer un nouveau round")
            print("2. 📝 Saisir les résultats du round en cours")
            print("3. 📊 Voir classement")
            print("4. 🔙 Retour")
            print("5. 🧾 Exporter le tournoi en HTML")

            action = input("Choix : ")

            if action == "1":
                nouveau_round = tournoi.start_new_round()
                if nouveau_round:
                    display.message_succes(f"Round lancé : {nouveau_round.nom}")
                self.data_manager.save_tournaments(tournois)

            elif action == "2":
                self.saisir_resultats(tournoi)
                self.data_manager.save_tournaments(tournois)

            elif action == "3":
                classement = tournoi.get_classement()
                display.afficher_classement(classement)

            elif action == "4":
                break

            elif action == "5":
                export_tournament_to_html(tournoi)

            else:
                display.message_erreur("Entrée invalide.")

    def saisir_resultats(self, tournoi):
        if not tournoi.rounds:
            display.message_erreur("Aucun round à remplir.")
            return

        round_en_cours = tournoi.rounds[-1]
        if round_en_cours.end_date:
            display.message_info("Ce round est déjà terminé.")
            return

        display.message_info(f"Résultats pour {round_en_cours.nom}")

        for match in round_en_cours.matchs:
            while True:
                print(f"\nMatch : {match.player1.first_name} vs {match.player2.first_name}")
                score_input = input("Résultat (format : 1-0, 0.5-0.5, 0-1) : ")

                try:
                    score1_str, score2_str = score_input.strip().split("-")
                    match.score1 = float(score1_str)
                    match.score2 = float(score2_str)

                    pair = (match.score1, match.score2)
                    if pair not in [(1.0, 0.0), (0.0, 1.0), (0.5, 0.5)]:
                        raise ValueError

                    match.player1.score += match.score1
                    match.player2.score += match.score2
                    break

                except (ValueError, IndexError):
                    display.message_erreur("⛔ Format invalide. Utilisez : 1-0, 0.5-0.5 ou 0-1.")

        round_en_cours.close_round()
        display.message_succes(f"Résultats enregistrés pour {round_en_cours.nom}.")

    def export_markdown(self):
        tournois = self.data_manager.load_tournaments()
        if not tournois:
            display.message_erreur("Aucun tournoi à exporter.")
            return

        print("\n=== 📄 EXPORT MARKDOWN ===")
        for i, tournoi in enumerate(tournois, 1):
            print(f"{i}. {tournoi.nom}")

        choix = input("Quel tournoi exporter ? : ")
        if not choix.isdigit() or not (1 <= int(choix) <= len(tournois)):
            display.message_erreur("Choix invalide.")
            return

        tournoi = tournois[int(choix) - 1]
        export_tournament_to_markdown(tournoi)

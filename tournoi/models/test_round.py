from models.tournament import Tournament

# Charger le tournoi existant
loaded_tournaments = Tournament.load_from_json()
tournament = loaded_tournaments[0] if loaded_tournaments else None

if tournament:
    new_round = tournament.start_new_round()  # Démarrer un nouveau round
    if new_round:
        tournament.save_to_json()
        print(f"[INFO] Nouveau round ajouté : {new_round.name}")

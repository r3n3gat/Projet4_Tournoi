def afficher_menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. 🎮 Gérer les joueurs")
    print("2. ♟️ Gérer les tournois")
    print("3. ❌ Quitter")


def afficher_liste_joueurs(joueurs):
    print("\n=== 📋 LISTE DES JOUEURS ===")
    if not joueurs:
        print("Aucun joueur disponible.")
        return

    print(f"{'ID':<10} {'Nom':<15} {'Prénom':<15} {'Naissance':<12} {'Score':<6}")
    print("-" * 60)
    for joueur in joueurs:
        print(f"{joueur.chess_id:<10} {joueur.last_name:<15} {joueur.first_name:<15} {joueur.birth_date:<12} {joueur.score:<6}")


def afficher_liste_tournois(tournois):
    print("\n=== 📅 LISTE DES TOURNOIS ===")
    if not tournois:
        print("Aucun tournoi enregistré.")
        return

    for i, t in enumerate(tournois, 1):
        print(f"{i}. {t.nom} - {t.lieu} ({t.date_debut} → {t.date_fin})")


def afficher_classement(joueurs):
    print("\n=== 📊 CLASSEMENT ACTUEL ===")
    if not joueurs:
        print("Aucun joueur.")
        return

    joueurs_tries = sorted(joueurs, key=lambda j: j.score, reverse=True)
    for i, joueur in enumerate(joueurs_tries, 1):
        print(f"{i}. {joueur.first_name} {joueur.last_name} - {joueur.score:.1f} pts")


def message_info(msg):
    print(f"[INFO] {msg}")


def message_succes(msg):
    print(f"[✅] {msg}")


def message_erreur(msg):
    print(f"[⛔] {msg}")

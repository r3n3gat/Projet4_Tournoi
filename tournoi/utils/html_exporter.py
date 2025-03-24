import os
from datetime import datetime


def export_tournament_to_html(tournoi):
    """Génère un fichier HTML lisible pour présenter un tournoi."""
    nom_fichier = f"tournoi_{tournoi.nom.lower().replace(' ', '_')}.html"
    dossier = "exports"
    os.makedirs(dossier, exist_ok=True)
    chemin_fichier = os.path.join(dossier, nom_fichier)

    with open(chemin_fichier, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='UTF-8'>")
        f.write("<title>Rapport Tournoi</title>")
        f.write("<style>")
        f.write("body { font-family: Arial; margin: 30px; }")
        f.write("table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }")
        f.write("th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }")
        f.write("th { background-color: #f2f2f2; }")
        f.write("</style>")
        f.write("</head><body>")

        # En-tête tournoi
        f.write(f"<h1>Tournoi : {tournoi.nom}</h1>")
        f.write(f"<p><strong>Lieu :</strong> {tournoi.lieu}<br>")
        f.write(f"<strong>Dates :</strong> {tournoi.date_debut} → {tournoi.date_fin}<br>")
        f.write(f"<strong>Remarques :</strong> {tournoi.remarques}</p>")

        # Classement joueurs
        joueurs = sorted(tournoi.joueurs, key=lambda j: j.score, reverse=True)
        f.write("<h2>Classement des joueurs</h2>")
        f.write("<table><tr><th>Nom</th><th>Prénom</th><th>ID</th><th>Score</th></tr>")
        for joueur in joueurs:
            f.write(f"<tr><td>{joueur.last_name}</td><td>{joueur.first_name}</td><td>{joueur.chess_id}</td><td>{joueur.score}</td></tr>")
        f.write("</table>")

        # Rounds et matchs
        for round_ in tournoi.rounds:
            f.write(f"<h3>{round_.nom}</h3>")
            f.write(f"<p><em>Début :</em> {round_.start_date} | <em>Fin :</em> {round_.end_date or 'en cours'}</p>")
            f.write("<table><tr><th>Joueur 1</th><th>Score</th><th>Joueur 2</th><th>Score</th></tr>")
            for match in round_.matchs:
                f.write(f"<tr><td>{match.player1.first_name} {match.player1.last_name}</td><td>{match.score1}</td>"
                        f"<td>{match.player2.first_name} {match.player2.last_name}</td><td>{match.score2}</td></tr>")
            f.write("</table>")

        f.write(f"<p><small>Exporté le {datetime.now().strftime('%d/%m/%Y %H:%M')}</small></p>")
        f.write("</body></html>")

    print(f"[✅] Rapport HTML généré : {chemin_fichier}")

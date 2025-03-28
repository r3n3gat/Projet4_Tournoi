import os


def export_tournament_to_html(tournoi):
    """
    Exporte un tournoi en fichier HTML (résumé des rounds, joueurs, scores).

    Args:
        tournoi (Tournament): objet tournoi à exporter
    """
    filename = f"tournoi_{tournoi.nom.lower().replace(' ', '_')}.html"
    export_folder = "exports"
    os.makedirs(export_folder, exist_ok=True)
    path = os.path.join(export_folder, filename)

    with open(path, "w", encoding="utf-8") as file:
        file.write("<html><head><meta charset='UTF-8'>")
        file.write(f"<title>{tournoi.nom}</title>")
        file.write("<style>")
        file.write("body { font-family: Arial; margin: 40px; }")
        file.write("h1 { color: #2c3e50; } table { border-collapse: collapse; width: 80%; }")
        file.write("th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }")
        file.write("th { background-color: #f4f4f4; }")
        file.write("</style></head><body>")

        file.write(f"<h1>Tournoi : {tournoi.nom}</h1>")
        file.write(f"<p><strong>Lieu :</strong> {tournoi.lieu}</p>")
        file.write(f"<p><strong>Dates :</strong> {tournoi.date_debut} → {tournoi.date_fin}</p>")
        file.write("<h2>Joueurs</h2><ul>")

        for joueur in tournoi.joueurs:
            nom = f"{joueur.first_name} {joueur.last_name}"
            file.write(f"<li>{nom} (ID : {joueur.chess_id})</li>")
        file.write("</ul>")

        for round_ in tournoi.rounds:
            file.write(f"<h3>{round_.nom}</h3>")
            file.write("<table><tr><th>Joueur 1</th><th>Score</th><th>Score</th><th>Joueur 2</th></tr>")
            for match in round_.matchs:
                p1 = match.player1
                p2 = match.player2
                file.write(
                    f"<tr><td>{p1.first_name} {p1.last_name}</td>"
                    f"<td>{match.score1}</td>"
                    f"<td>{match.score2}</td>"
                    f"<td>{p2.first_name} {p2.last_name}</td></tr>"
                )
            file.write("</table>")

        file.write("</body></html>")

    print(f" Rapport HTML généré : {path}")

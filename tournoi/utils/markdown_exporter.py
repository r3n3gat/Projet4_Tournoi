import os
from datetime import datetime


def export_tournament_to_markdown(tournoi):
    """
    Exporte un tournoi au format Markdown dans le dossier 'exports/'.
    Le fichier est nommé : rapport_<nom-tournoi>_<datetime>.md
    """
    os.makedirs("exports", exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nom_fichier = f"exports/rapport_{tournoi.nom.lower().replace(' ', '_')}_{now}.md"

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"# Rapport du tournoi : {tournoi.nom}\n\n")
        f.write(f"**Lieu :** {tournoi.lieu}\n\n")
        f.write(f"**Dates :** du {tournoi.date_debut} au {tournoi.date_fin}\n\n")
        f.write(f"_Rapport généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}_\n\n")

        if tournoi.remarques:
            f.write(f"**Remarques :** {tournoi.remarques}\n\n")

        f.write("\n---\n\n")
        f.write("## Joueurs participants\n\n")
        for joueur in tournoi.joueurs:
            f.write(
                f"- {joueur.first_name} {joueur.last_name} "
                f"(ID: {joueur.chess_id}, Score: {joueur.score})\n"
            )

        f.write("\n---\n\n")
        f.write("## Rounds et matchs\n\n")
        for round_ in tournoi.rounds:
            f.write(f"### {round_.nom}\n")
            f.write(f"Début : {round_.start_date}\n")
            f.write(f"Fin : {round_.end_date or 'En cours'}\n\n")

            for match in round_.matchs:
                f.write(
                    f"- {match.player1.first_name} {match.player1.last_name} "
                    f"vs {match.player2.first_name} {match.player2.last_name} "
                    f"→ {match.score1} - {match.score2}\n"
                )
            f.write("\n")

    print(f" Rapport Markdown généré : {nom_fichier}")

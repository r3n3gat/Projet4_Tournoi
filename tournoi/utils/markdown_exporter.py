import os
from datetime import datetime


def export_tournament_to_markdown(tournoi):
    """Génère un rapport Markdown (.md) du tournoi sélectionné."""

    # Nettoyage du nom pour le nom de fichier
    slug = tournoi.nom.lower().replace(" ", "_")
    filename = f"rapport_{slug}.md"
    export_path = os.path.join("exports", filename)
    os.makedirs("exports", exist_ok=True)

    with open(export_path, "w", encoding="utf-8") as f:
        # ✅ En-tête
        f.write(f"# 🏆 Rapport du tournoi : {tournoi.nom}\n\n")
        f.write(f"- **Lieu :** {tournoi.lieu}\n")
        f.write(f"- **Dates :** du {tournoi.date_debut} au {tournoi.date_fin}\n")
        f.write(f"- **Remarques :** {tournoi.remarques or 'Aucune'}\n\n")

        # ✅ Classement des joueurs
        classement = tournoi.get_classement()
        f.write("## 📊 Classement final\n\n")
        f.write("| Rang | Nom | Prénom | Score |\n")
        f.write("|------|-----|--------|-------|\n")
        for i, joueur in enumerate(classement, 1):
            f.write(f"| {i} | {joueur.last_name} | {joueur.first_name} | {joueur.score} |\n")
        f.write("\n")

        # ✅ Détail des rounds
        f.write("## 🕒 Détail des rounds\n\n")
        for round_ in tournoi.rounds:
            f.write(f"### {round_.nom}\n")
            f.write(f"- Début : {round_.start_date}\n")
            f.write(f"- Fin : {round_.end_date or 'Non terminé'}\n\n")
            f.write("| Joueur 1 | Score | Joueur 2 | Score |\n")
            f.write("|----------|-------|----------|-------|\n")
            for match in round_.matchs:
                f.write(f"| {match.player1.last_name} | {match.score1} | {match.player2.last_name} | {match.score2} |\n")
            f.write("\n")

        f.write(f"---\n*Exporté le {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")

    print(f"[✅] Rapport Markdown généré : {export_path}")

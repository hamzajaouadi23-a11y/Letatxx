#!/usr/bin/env bash
# run.sh — lance les automatisations du dossier de réorientation.
#
#   bash outils/run.sh all            tout générer (CV + candidatures + relances + liens + PDF)
#   bash outils/run.sh cv             générer le CV (Markdown + PDF) depuis profil.json
#   bash outils/run.sh candidatures   générer les e-mails/lettres par entreprise
#   bash outils/run.sh relances       qui relancer aujourd'hui
#   bash outils/run.sh journee        plan de prospection de la journée
#   bash outils/run.sh liens          imprimer les URLs de recherche pré-remplies
#   bash outils/run.sh pdf            convertir les documents Markdown en PDF
#   bash outils/run.sh dashboard      lancer le tableau de bord web (http://0.0.0.0:8080)
#   bash outils/run.sh statut         statistiques rapides
set -euo pipefail

RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RACINE"
ACTION="${1:-all}"
PORT="${PORT:-8080}"

case "$ACTION" in
  cv)           python3 outils/generer_cv.py ;;
  candidatures) python3 outils/generer_candidatures.py ;;
  relances)     python3 outils/relances.py --texte ;;
  journee)      python3 outils/relances.py --journee ;;
  liens)        python3 outils/urls_recherche.py --html ;;
  pdf)          python3 outils/md2pdf.py ;;
  statut)       python3 outils/relances.py --statistiques ;;
  dashboard)    PORT="$PORT" python3 outils/dashboard.py ;;
  all)
    echo "── 1/5 CV ──"; python3 outils/generer_cv.py
    echo; echo "── 2/5 candidatures ──"; python3 outils/generer_candidatures.py
    echo; echo "── 3/5 liens de recherche ──"; python3 outils/urls_recherche.py --html | tail -2
    echo; echo "── 4/5 PDF du dossier ──"; python3 outils/md2pdf.py | tail -3
    echo; echo "── 5/5 relances dues ──"; python3 outils/relances.py
    echo; echo "Terminé. Pour le tableau de bord : bash outils/run.sh dashboard"
    ;;
  *) echo "Action inconnue : $ACTION (voir l'en-tête de ce fichier)"; exit 1 ;;
esac

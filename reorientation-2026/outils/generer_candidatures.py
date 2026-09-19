#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generer_candidatures.py — produit, pour chaque entreprise du tracker, un dossier prêt à envoyer :
    generes/<entreprise>/email.txt        e-mail court de candidature
    generes/<entreprise>/lettre.txt       lettre de motivation (version A/B/C/D selon le secteur)
    generes/<entreprise>/notes_appel.txt  fiche d'appel téléphonique
    generes/<entreprise>/fiche.md         synthèse (angle, canal, contact, version)
Plus :
    generes/index.md                      sommaire cliquable
    generes/a_envoyer.csv                 fichier d'envoi (objet, destinataire, chemin)

Exemples :
    python3 outils/generer_candidatures.py                 # toutes les cibles actives
    python3 outils/generer_candidatures.py --priorite 1    # uniquement la priorité 1
    python3 outils/generer_candidatures.py --ids 1,2,5     # cibles précises
    python3 outils/generer_candidatures.py --tout          # y compris les cibles clôturées
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_tracker as T  # noqa: E402
import modeles as M      # noqa: E402


def selection(lignes, ids=None, priorite=None, tout=False):
    out = []
    for l in lignes:
        statut = (l.get("statut") or "a_contacter").strip()
        if not tout and statut in T.STATUTS_TERMINES:
            continue
        if ids and str(l.get("id")) not in ids:
            continue
        if priorite and str(l.get("priorite")) != str(priorite):
            continue
        out.append(l)
    return out


def generer(ligne: dict) -> dict:
    ctx = T.contexte(ligne)
    dossier = T.GENERS / f"{int(ligne.get('id') or 0):02d}-{T.slug(ligne.get('entreprise'))}"
    dossier.mkdir(parents=True, exist_ok=True)

    version = T.version_lettre(ligne)
    textes = {
        "email.txt": T.remplir(M.EMAIL_CANDIDATURE, ctx),
        "lettre.txt": T.remplir(M.LETTRES[version], ctx),
        "notes_appel.txt": T.remplir(M.NOTES_APPEL, ctx),
        "relance_j4.txt": T.remplir(M.RELANCE_J4, ctx),
        "relance_j10.txt": T.remplir(M.RELANCE_J10, ctx),
        "relance_j20.txt": T.remplir(M.RELANCE_J20, ctx),
        "remerciement.txt": T.remplir(M.REMERCIEMENT_ENTRETIEN, ctx),
    }
    manquants = set()
    for nom, texte in textes.items():
        (dossier / nom).write_text(texte, encoding="utf-8")
        manquants.update(T.tokens_manquants(texte))

    fiche = f"""# {ligne.get('entreprise')} — cible n°{ligne.get('id')}

| | |
|---|---|
| **Statut** | {T.STATUT_LABELS.get(ligne.get('statut'), ligne.get('statut'))} |
| **Priorité** | {ligne.get('priorite')} |
| **Secteur** | {ligne.get('secteur')} |
| **Ville** | {ligne.get('ville')} · taille estimée : {ligne.get('taille')} |
| **Poste visé** | {ligne.get('poste_vise')} |
| **Canal** | {ligne.get('canal')} |
| **Contact** | {ligne.get('contact') or '⟦à identifier⟧'} |
| **Coordonnées** | {ligne.get('email_url') or '⟦à compléter⟧'} |
| **Version de lettre** | {version} |

## Angle d'attaque
{ligne.get('angle')}

## Notes
{ligne.get('notes') or '—'}

## Prochaine action
{ligne.get('prochaine_action') or '—'}

## Fichiers prêts à envoyer
- `email.txt` — e-mail court de candidature
- `lettre.txt` — lettre de motivation (version {version})
- `notes_appel.txt` — fiche d'appel téléphonique
- `relance_j4.txt`, `relance_j10.txt`, `relance_j20.txt` — séquence de relance
- `remerciement.txt` — message post-entretien
"""
    (dossier / "fiche.md").write_text(fiche, encoding="utf-8")
    return {"dossier": dossier, "version": version, "manquants": sorted(manquants), "ctx": ctx}


def objet(ligne: dict, ctx: dict) -> str:
    return T.remplir(
        "Alternance BTS Commerce International — assistant {{POSTE_VISE}} — {{ENTREPRISE}}", ctx
    ).strip()


def main() -> int:
    ap = argparse.ArgumentParser(description="Génère les candidatures personnalisées.")
    ap.add_argument("--ids", help="liste d'identifiants séparés par des virgules")
    ap.add_argument("--priorite", help="1, 2 ou 3")
    ap.add_argument("--tout", action="store_true", help="inclure les cibles clôturées")
    args = ap.parse_args()

    ids = set(s.strip() for s in args.ids.split(",")) if args.ids else None
    lignes = T.charger_lignes()
    cibles = selection(lignes, ids, args.priorite, args.tout)
    if not cibles:
        print("Aucune cible ne correspond à ces filtres.")
        return 1

    T.GENERS.mkdir(parents=True, exist_ok=True)
    resultats = []
    for ligne in cibles:
        resultats.append((ligne, generer(ligne)))

    # index.md
    entetes = ["id", "entreprise", "ville", "priorite", "statut", "version_lettre",
               "email", "lettre", "notes_appel", "tokens_manquants"]
    lignes_index = []
    for ligne, res in resultats:
        rel = res["dossier"].relative_to(T.GENERS).as_posix()
        lignes_index.append({
            "id": ligne.get("id"),
            "entreprise": ligne.get("entreprise"),
            "ville": ligne.get("ville"),
            "priorite": ligne.get("priorite"),
            "statut": ligne.get("statut"),
            "version_lettre": res["version"],
            "email": f"generes/{rel}/email.txt",
            "lettre": f"generes/{rel}/lettre.txt",
            "notes_appel": f"generes/{rel}/notes_appel.txt",
            "tokens_manquants": " ".join(res["manquants"]),
        })
    with (T.GENERS / "a_envoyer.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=entetes + ["objet", "destinataire"])
        w.writeheader()
        for ligne, res in resultats:
            row = next(r for r in lignes_index if r["id"] == ligne.get("id"))
            row["objet"] = objet(ligne, res["ctx"]).replace("\n", " ")
            row["destinataire"] = ligne.get("email_url") or "⟦à compléter⟧"
            w.writerow(row)

    md = ["# Candidatures générées\n",
          f"Généré le {T.fmt_date(T.aujourdhui())} — {len(resultats)} cibles.\n",
          "| ID | Priorité | Entreprise | Ville | Lettre | Statut | E-mail | Lettre | Appel |",
          "|---|---|---|---|---|---|---|---|---|"]
    for ligne, res in resultats:
        rel = res["dossier"].relative_to(T.GENERS).as_posix()
        md.append("| {id} | {p} | **{e}** | {v} | {lettre} | {s} | [email]({r}/email.txt) | "
                  "[lettre]({r}/lettre.txt) | [appel]({r}/notes_appel.txt) |".format(
                      id=ligne.get("id"), p=ligne.get("priorite"), e=ligne.get("entreprise"),
                      v=ligne.get("ville"), lettre=res["version"],
                      s=ligne.get("statut"), r=rel))
    manquants_global = sorted({m for _, res in resultats for m in res["manquants"]})
    md.append("\n## Champs à compléter dans `outils/profil.json` ou `outils/tracker.csv`\n")
    if manquants_global:
        md.append("Les tokens suivants apparaissent encore sous la forme ⟦TOKEN⟧ dans les textes générés :\n")
        for t in manquants_global:
            md.append(f"- `{{{t}}}`")
    else:
        md.append("Aucun : tous les champs nécessaires sont renseignés. 🎉")
    (T.GENERS / "index.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"✔ {len(resultats)} dossiers de candidature générés dans outils/generes/")
    print(f"  - sommaire : outils/generes/index.md")
    print(f"  - fichier d'envoi : outils/generes/a_envoyer.csv")
    if manquants_global:
        print(f"⚠ {len(manquants_global)} champ(s) encore à compléter : {', '.join(manquants_global)}")
        print("  → remplis outils/profil.json (identité, langues) et/ou la colonne 'contact' du tracker.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

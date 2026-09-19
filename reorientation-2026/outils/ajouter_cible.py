#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ajouter_cible.py — ajoute une entreprise au tracker sans ouvrir le CSV.

    python3 outils/ajouter_cible.py --entreprise "Transit Express Marseille" \\
        --ville "Marseille 15e" --secteur "Transit / douane" --taille PME \\
        --poste "assistant import-export" \\
        --angle "PME de transit maritime, besoin de renfort sur la saisie des dossiers" \\
        --priorite 2 --canal "Téléphone + e-mail" --url "https://exemple.fr"

    python3 outils/ajouter_cible.py --import-annuaire fichier.csv
        (fichier CSV avec au minimum les colonnes : entreprise, ville, secteur)
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_tracker as T  # noqa: E402


def nouvelle_ligne(champs: dict, ident: int) -> dict:
    ligne = dict.fromkeys(T.entetes(), "")
    ligne.update({
        "id": str(ident),
        "statut": "a_contacter",
        "priorite": "2",
        "entreprise": "",
        "secteur": "",
        "ville": "",
        "taille": "",
        "poste_vise": "assistant import-export",
        "angle": "",
        "canal": "E-mail + téléphone",
    })
    ligne.update({k: v for k, v in champs.items() if v})
    return ligne


def prochain_id(lignes: list) -> int:
    ids = [int(l["id"]) for l in lignes if str(l.get("id", "")).strip().isdigit()]
    return (max(ids) + 1) if ids else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Ajoute une ou plusieurs cibles au tracker.")
    ap.add_argument("--entreprise")
    ap.add_argument("--ville")
    ap.add_argument("--secteur")
    ap.add_argument("--taille", help="TPE, PME, TPE-PME, ETI, Grand groupe")
    ap.add_argument("--poste", dest="poste_vise")
    ap.add_argument("--angle", help="pourquoi cette entreprise, quel argument d'entrée")
    ap.add_argument("--priorite", default="2", choices=["1", "2", "3"])
    ap.add_argument("--canal")
    ap.add_argument("--contact", help="nom + fonction de l'interlocuteur")
    ap.add_argument("--url", dest="email_url", help="e-mail ou URL du site / page carrières")
    ap.add_argument("--notes")
    ap.add_argument("--import-annuaire", help="CSV à importer (colonnes entreprise, ville, secteur…)")
    args = ap.parse_args()

    lignes = T.charger_lignes()
    ajoutees = []

    if args.import_annuaire:
        chemin = Path(args.import_annuaire)
        if not chemin.exists():
            print(f"✘ fichier introuvable : {chemin}")
            return 1
        with chemin.open(newline="", encoding="utf-8-sig") as fh:
            for ligne in csv.DictReader(fh):
                if not (ligne.get("entreprise") or "").strip():
                    continue
                if any((l.get("entreprise") or "").strip().lower() == ligne["entreprise"].strip().lower()
                       for l in lignes):
                    print(f"– déjà présent : {ligne['entreprise']}")
                    continue
                nouv = nouvelle_ligne({k: (v or "").strip() for k, v in ligne.items()
                                       if k in T.entetes()}, prochain_id(lignes))
                lignes.append(nouv)
                ajoutees.append(nouv["entreprise"])
    elif args.entreprise:
        if any((l.get("entreprise") or "").strip().lower() == args.entreprise.strip().lower() for l in lignes):
            print(f"– déjà présent dans le tracker : {args.entreprise}")
            return 0
        champs = {k: v for k, v in vars(args).items()
                  if k in T.entetes() and v and k != "import_annuaire"}
        nouv = nouvelle_ligne(champs, prochain_id(lignes))
        lignes.append(nouv)
        ajoutees.append(nouv["entreprise"])
    else:
        ap.print_help()
        return 1

    T.enregistrer_lignes(lignes)
    for nom in ajoutees:
        print(f"✔ ajouté : {nom}")
    print(f"  total du tracker : {len(lignes)} cibles")
    print("  → python3 outils/generer_candidatures.py   (pour produire les textes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

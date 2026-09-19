#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
relances.py — chaque matin, te dit QUI contacter et te donne le TEXTE exact à coller.

Exemples :
    python3 outils/relances.py                    actions dues + échéances
    python3 outils/relances.py --texte            affiche aussi les textes prêts à coller
    python3 outils/relances.py --journee          le plan de la journée (appels + e-mails)
    python3 outils/relances.py --maj 3:envoye     marque la cible 3 comme « candidature envoyée » (date du jour)
    python3 outils/relances.py --maj 7:entretien --maj 12:relance1
    python3 outils/relances.py --statistiques     tableau de bord chiffré
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_tracker as T  # noqa: E402
import modeles as M      # noqa: E402

SUIVANTE = {"a_contacter": "envoye", "contacte": "envoye", "envoye": "relance1",
            "relance1": "relance2", "relance2": "sans_reponse", "entretien": "offre",
            "offre": "gagne"}

TEXTE_PAR_STATUT = {
    "contacte": M.EMAIL_CANDIDATURE,
    "envoye": M.RELANCE_J4,
    "relance1": M.RELANCE_J10,
    "relance2": M.RELANCE_J20,
    "entretien": M.RELANCE_APRES_ENTRETIEN,
}


def texte_du_jour(ligne: dict) -> str:
    statut = (ligne.get("statut") or "").strip()
    modele = TEXTE_PAR_STATUT.get(statut)
    if modele is None:
        return M.EMAIL_CANDIDATURE
    return T.remplir(modele, T.contexte(ligne))


def afficher_echeances() -> None:
    print("\n" + "=" * 78)
    print("ÉCHÉANCES")
    print("=" * 78)
    for e in T.echeances():
        j = e["jours"]
        if j < 0:
            marque = f"⛔ DÉPASSÉE de {abs(j)} j"
        elif j == 0:
            marque = "🔥 AUJOURD'HUI"
        elif j <= 7:
            marque = f"⚠ dans {j} j"
        else:
            marque = f"dans {j} j"
        print(f"  {T.fmt_date(e['date'])}  {marque:<22} {e['libelle']}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Relances dues et plan de prospection du jour.")
    ap.add_argument("--texte", action="store_true", help="afficher le texte prêt à coller")
    ap.add_argument("--journee", action="store_true", help="plan de la journée (appels + e-mails)")
    ap.add_argument("--statistiques", action="store_true")
    ap.add_argument("--maj", action="append", default=[], metavar="ID:STATUT",
                    help="met à jour une cible, ex. 3:envoye")
    args = ap.parse_args()

    lignes = T.charger_lignes()
    aujourd = T.aujourdhui()

    if args.maj:
        cibles = {str(l.get("id")): l for l in lignes}
        for maj in args.maj:
            if ":" not in maj:
                print(f"⚠ format attendu ID:STATUT, reçu « {maj} »")
                continue
            ident, statut = maj.split(":", 1)
            statut = statut.strip()
            if ident.strip() not in cibles:
                print(f"⚠ identifiant inconnu : {ident}")
                continue
            if statut not in T.STATUT_LABELS:
                print(f"⚠ statut inconnu : {statut} — choix : {', '.join(T.STATUT_LABELS)}")
                continue
            cible = cibles[ident.strip()]
            cible["statut"] = statut
            cible["date_envoi"] = T.fmt_date(aujourd)
            cible["prochaine_action"] = ""
            print(f"✔ {cible['entreprise']} → {T.STATUT_LABELS[statut]} (action datée du {T.fmt_date(aujourd)})")
        T.enregistrer_lignes(lignes)

    stats = T.statistiques(lignes)
    if args.statistiques:
        print("=" * 78)
        print(f"STATISTIQUES — {stats['total']} cibles au total, {stats['actifs']} actives")
        print("=" * 78)
        for cle, libelle in T.STATUTS:
            barre = "█" * stats.get(cle, 0)
            print(f"  {libelle:<34} {stats.get(cle, 0):>3}  {barre}")

    dues = T.relances_dues(lignes, aujourd)
    print("\n" + "=" * 78)
    print(f"ACTIONS DUES AU {T.fmt_date(aujourd)} — {len(dues)} cible(s)")
    print("=" * 78)
    if not dues:
        print("  Rien à faire aujourd'hui : tout est à jour. 👌")
    for i, d in enumerate(dues, 1):
        l = d["ligne"]
        retard = f" (retard {d['retard']} j)" if d["retard"] else ""
        print(f"\n{i:>2}. [{l.get('id')}] {l.get('entreprise')} — {l.get('ville')} (priorité {l.get('priorite')})")
        print(f"    statut : {T.STATUT_LABELS.get(l.get('statut'), l.get('statut'))} · dernière action : "
              f"{T.fmt_date(l.get('date_envoi')) or 'non renseignée'}{retard}")
        print(f"    → {d['etiquette']}")
        print(f"    contact : {l.get('contact') or '⟦à identifier⟧'} · {l.get('email_url') or l.get('canal')}")
        print(f"    mise à jour après envoi :  python3 outils/relances.py --maj {l.get('id')}:"
              f"{SUIVANTE.get((l.get('statut') or '').strip(), 'relance1')}")
        if args.texte:
            print("    " + "-" * 70)
            for ln in texte_du_jour(l).rstrip().splitlines():
                print(f"    {ln}")

    if args.journee:
        print("\n" + "=" * 78)
        print("PLAN DE LA JOURNÉE (45 à 90 minutes)")
        print("=" * 78)
        a_appeler = [d["ligne"] for d in dues if (d["ligne"].get("taille") or "").upper() in ("TPE", "PME", "TPE-PME")
                     or "PME" in (d["ligne"].get("taille") or "")]
        a_appeler += [d["ligne"] for d in dues if d["ligne"] not in a_appeler]
        print("\n① 10 appels téléphoniques (les PME d'abord, on décroche plus qu'on ne lit) :")
        for l in a_appeler[:10]:
            tel = l.get("email_url") or ""
            print(f"   ☎  [{l.get('id')}] {l.get('entreprise')} — {l.get('ville')} {tel}")
        print("\n② 10 e-mails personnalisés (générés dans outils/generes/) :")
        for d in dues[:10]:
            l = d["ligne"]
            print(f"   ✉  [{l.get('id')}] {l.get('entreprise')} → {d['etiquette']}")
        print("\n③ 5 actions réseau :")
        print("   • 5 connexions LinkedIn avec note personnelle (modèle dans emails-candidature.md)")
        print("   • 1 demande d'introduction à ton père (transitaire, négociant, client importateur)")
        print("   • 1 message à l'IFC (offres partenaires non pourvues)")
        print("\n④ 5 minutes de mise à jour du tracker (sinon tu perds le fil en 48 h).")

    afficher_echeances()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

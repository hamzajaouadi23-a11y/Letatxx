#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lib_tracker.py — bibliothèque partagée du dossier de réorientation.

Rôle : lire/écrire tracker.csv, charger profil.json et config.json, remplir les modèles
à trous ({{TOKEN}}), calculer les relances dues et les échéances.

Aucune dépendance externe : Python 3.8+ standard.
"""
from __future__ import annotations

import csv
import json
import re
import unicodedata
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOSSIER = ROOT.parent
TRACKER = ROOT / "tracker.csv"
PROFIL = ROOT / "profil.json"
CONFIG = ROOT / "config.json"
GENERS = ROOT / "generes"

# --- Modèle de statuts -------------------------------------------------------
STATUTS = [
    ("a_contacter", "À contacter"),
    ("contacte", "Contacté (appel / message)"),
    ("envoye", "Candidature envoyée"),
    ("relance1", "Relance 1 faite"),
    ("relance2", "Relance 2 faite"),
    ("entretien", "Entretien obtenu"),
    ("offre", "Offre reçue"),
    ("gagne", "Contrat signé"),
    ("refuse", "Refusé"),
    ("sans_reponse", "Sans réponse (clôturé)"),
]
STATUT_LABELS = dict(STATUTS)
STATUT_ACTIFS = {"a_contacter", "contacte", "envoye", "relance1", "relance2", "entretien", "offre"}
STATUTS_TERMINES = {"gagne", "refuse", "sans_reponse"}

SEUILS_DEFAUT = {"contacte": 4, "envoye": 4, "relance1": 10, "relance2": 20, "entretien": 3}

JOURS_FR = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]


# --- Chargements -------------------------------------------------------------
def aujourdhui() -> date:
    return date.today()


def parse_date(valeur: str):
    if not valeur:
        return None
    valeur = valeur.strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d/%m/%y"):
        try:
            return datetime.strptime(valeur, fmt).date()
        except ValueError:
            continue
    return None


def fmt_date(d) -> str:
    if isinstance(d, str):
        d = parse_date(d)
    return d.strftime("%d/%m/%Y") if d else ""


def charger_lignes() -> list:
    """Retourne la liste des lignes du tracker (list de dict)."""
    if not TRACKER.exists():
        raise SystemExit(f"tracker.csv introuvable : {TRACKER}")
    with TRACKER.open(newline="", encoding="utf-8-sig") as fh:
        lecteur = csv.DictReader(fh)
        lignes = [dict(l) for l in lecteur if (l.get("entreprise") or "").strip()]
        entetes = lecteur.fieldnames or []
    for l in lignes:
        for k in entetes:
            l.setdefault(k, "")
    return lignes


def entetes() -> list:
    with TRACKER.open(newline="", encoding="utf-8-sig") as fh:
        return next(csv.reader(fh))


def enregistrer_lignes(lignes: list) -> None:
    champs = entetes()
    with TRACKER.open("w", newline="", encoding="utf-8") as fh:
        ecrivain = csv.DictWriter(fh, fieldnames=champs)
        ecrivain.writeheader()
        for l in lignes:
            ecrivain.writerow({c: l.get(c, "") for c in champs})


def _charger_json(chemin: Path, defaut):
    if not chemin.exists():
        return defaut
    try:
        with chemin.open(encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        print(f"⚠ JSON invalide dans {chemin.name} : {exc}")
        return defaut


def profil() -> dict:
    return _charger_json(PROFIL, {})


def config() -> dict:
    return _charger_json(CONFIG, {})


def seuils() -> dict:
    cfg = config().get("seuils_relance_jours") or {}
    out = dict(SEUILS_DEFAUT)
    out.update({k: int(v) for k, v in cfg.items() if str(v).isdigit()})
    return out


# --- Texte : tokens et helpers ----------------------------------------------
def sans_accent(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s or "") if unicodedata.category(c) != "Mn")


def slug(s: str) -> str:
    s = sans_accent(s or "").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "cible"


def tronquer_propre(texte: str, maxi: int = 95) -> str:
    texte = (texte or "").strip()
    if len(texte) <= maxi:
        return texte
    coupe = texte[:maxi]
    if " " in coupe:
        coupe = coupe.rsplit(" ", 1)[0]
    return coupe.rstrip(" ,;:") + "…"


def minuscule_initiale(texte: str) -> str:
    """Met la première lettre en minuscule (pour insérer proprement un angle après « : »)."""
    texte = (texte or "").strip()
    if not texte:
        return texte
    return texte[0].lower() + texte[1:]


def angle_court(ligne: dict) -> str:
    angle = (ligne.get("angle") or "").strip()
    premiere = re.split(r"[.;]\s", angle)[0]
    return tronquer_propre(premiere, 95)


def prenom_contact(ligne: dict) -> str:
    contact = (ligne.get("contact") or "").strip()
    if not contact or contact.startswith("["):
        return "Madame, Monsieur"
    return contact.split()[0]


def prochain_jour_de_relance(offset: int = 2) -> str:
    d = aujourdhui() + timedelta(days=offset)
    while d.weekday() >= 5:  # on évite samedi/dimanche
        d += timedelta(days=1)
    return f"{JOURS_FR[d.weekday()]} prochain"


def contexte(ligne: dict) -> dict:
    """Fusionne le profil et la ligne du tracker en un dictionnaire de tokens {{MAJUSCULES}}."""
    ctx = {}
    prof = profil()
    for cle, val in prof.items():
        if cle.startswith("_"):
            continue
        if isinstance(val, list):
            if val and all(isinstance(v, dict) for v in val):
                # expériences : une ligne lisible par élément
                val = "\n".join(
                    "{periode}\t{poste} — {entreprise}, {ville}\n\t\t{detail}".format(
                        periode=v.get("periode", ""), poste=v.get("poste", ""),
                        entreprise=v.get("entreprise", ""), ville=v.get("ville", ""),
                        detail=v.get("detail", ""))
                    for v in val)
            else:
                val = ", ".join(str(v) for v in val)
        ctx[cle.upper()] = str(val)
    for cle, val in ligne.items():
        if not cle:  # tolère les lignes CSV mal formées (colonnes surnuméraires)
            continue
        ctx[str(cle).upper()] = str(val if val is not None else "")
    cfg = config()
    ctx.setdefault("DATE_RENTREE_IFC", cfg.get("date_rentree_ifc") or "à confirmer avec l'IFC")
    # dérivés
    ctx["ANGLE_COURT"] = minuscule_initiale(angle_court(ligne))
    ctx["PRENOM_CONTACT"] = prenom_contact(ligne)
    ctx["JOUR_APPEL"] = prochain_jour_de_relance(2)
    ctx["DATE_LIMITE"] = fmt_date(aujourdhui() + timedelta(days=5))
    ctx["DATE_DU_JOUR"] = fmt_date(aujourdhui())
    ctx["DATE_ENVOI_LUE"] = fmt_date(ligne.get("date_envoi")) or "ma candidature récente"
    ctx["APPORT"] = (profil().get("apport_relance") or "").strip() or "un élément concret sur votre activité"
    ctx["POINT_PRECIS"] = "[point précis évoqué en entretien]"
    poste_vise = (ligne.get("poste_vise") or "import-export").strip()
    ctx["POSTE_VISE"] = poste_vise
    bas = poste_vise.lower()
    if bas.startswith(("assistant", "assistante", "alternance", "contrat", "apprenti")):
        ctx["POSTE"] = minuscule_initiale(poste_vise)
    else:
        ctx["POSTE"] = "assistant " + minuscule_initiale(poste_vise)
    ctx["ENTREPRISE"] = (ligne.get("entreprise") or "").strip()
    ctx["VILLE"] = (ligne.get("ville") or "").strip()
    return ctx


TOKEN_RE = re.compile(r"\{\{\s*([A-Z0-9_]+)\s*\}\}")


def remplir(texte: str, ctx: dict) -> str:
    """Remplace les {{TOKENS}} ; laisse en place (en évidence) ce qui n'est pas renseigné."""
    def _sub(m):
        cle = m.group(1)
        val = ctx.get(cle)
        if val is None:
            return f"⟦{cle}⟧"
        val = str(val).strip()
        return val if val else f"⟦{cle}⟧"
    out = TOKEN_RE.sub(_sub, texte)
    return re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"


def tokens_manquants(texte: str) -> list:
    return sorted(set(re.findall(r"⟦([A-Z0-9_]+)⟧", texte)))


# --- Logique métier ----------------------------------------------------------
def version_lettre(ligne: dict) -> str:
    """A = transitaire/logistique, B = négoce PME, C = grand groupe, D = réseau proche."""
    entreprise = (ligne.get("entreprise") or "").lower()
    if "marée albe" in entreprise or "maree albe" in entreprise:
        return "D"
    champs = f"{ligne.get('secteur','')} {ligne.get('angle','')} {ligne.get('entreprise','')}".lower()
    grands = ("cma cgm", "maersk", "msc", "dsv", "geodis", "schenker", "kuehne", "dhl", "ceva",
              "pernod", "boisset", "bpifrance", "grand port")
    if any(g in champs for g in grands) or "grand groupe" in champs:
        return "C"
    transit = ("transit", "douane", "commissionnaire", "logistique", "freight", "port", "shipping",
               "armateur", "supply")
    if any(t in champs for t in transit):
        return "A"
    return "B"


def prochaine_action(ligne: dict, aujourd: date = None):
    """Retourne (due: bool, etiquette: str, retard_jours: int|None)."""
    aujourd = aujourd or aujourdhui()
    statut = (ligne.get("statut") or "a_contacter").strip()
    if statut in STATUTS_TERMINES:
        return False, "", None
    if statut == "a_contacter":
        return True, "Envoyer la première candidature (ou appeler)", None
    seuil = seuils().get(statut)
    if seuil is None:
        return False, "", None
    derniere = parse_date(ligne.get("date_envoi"))
    if derniere is None:
        return True, f"{STATUT_LABELS.get(statut, statut)} — date la dernière action dans le tracker", None
    ecart = (aujourd - derniere).days
    if ecart >= seuil:
        if statut == "entretien":
            etiquette = "Relancer après entretien + message de remerciement si ce n'est pas fait"
        elif statut == "contacte":
            etiquette = "Envoyer la candidature écrite (l'appel ne suffit pas)"
        elif statut == "relance1":
            etiquette = "Relance 2 — apporter une valeur (le « mini-tableau »)"
        elif statut == "relance2":
            etiquette = "Relance 3 — clôture (« je finalise mon choix »)"
        else:
            etiquette = "Relance 1 — la plus rentable de toutes"
        return True, etiquette, ecart
    return False, f"Prochaine relance dans {seuil - ecart} j", None


def echeances(aujourd: date = None) -> list:
    cfg = config()
    aujourd = aujourd or aujourdhui()
    items = [
        ("Dépôt demande annulation + remboursement AMU (objectif interne)", cfg.get("date_limite_amu")),
        ("Date limite AMU constatée (au-delà : rejet)", cfg.get("date_limite_amu_officielle")),
        ("Fin des candidatures IFC (limite des places disponibles)", cfg.get("date_limite_ifc")),
        ("Fin de la fenêtre de 3 mois pour signer un contrat d'apprentissage", cfg.get("date_limite_contrat_apprentissage")),
    ]
    out = []
    for libelle, valeur in items:
        d = parse_date(valeur or "")
        if not d:
            continue
        out.append({"libelle": libelle, "date": d, "jours": (d - aujourd).days})
    return sorted(out, key=lambda x: x["jours"])


def statistiques(lignes: list) -> dict:
    stats = {cle: 0 for cle, _ in STATUTS}
    for l in lignes:
        s = (l.get("statut") or "a_contacter").strip()
        stats[s] = stats.get(s, 0) + 1
    stats["total"] = len(lignes)
    stats["actifs"] = sum(v for k, v in stats.items() if k in STATUT_ACTIFS)
    return stats


def relances_dues(lignes: list, aujourd: date = None) -> list:
    dues = []
    for l in lignes:
        due, etiquette, retard = prochaine_action(l, aujourd)
        if due:
            dues.append({"ligne": l, "etiquette": etiquette, "retard": retard})
    ordre = {"entretien": 0, "offre": 1, "envoye": 2, "contacte": 2, "relance1": 3, "relance2": 4, "a_contacter": 5}
    dues.sort(key=lambda d: (ordre.get((d["ligne"].get("statut") or "a_contacter"), 9),
                             int(d["ligne"].get("priorite") or 9),
                             d["ligne"].get("entreprise", "")))
    return dues

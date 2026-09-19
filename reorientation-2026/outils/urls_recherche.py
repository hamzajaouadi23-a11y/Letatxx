#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
urls_recherche.py — imprime (ou ouvre) toutes les recherches pré-remplies utiles :
job boards, annuaires d'entreprises, LinkedIn, dispositifs publics.

Le sandbox n'a pas d'accès Internet : ces liens sont faits pour être ouverts depuis ton
navigateur. `--html` produit un fichier cliquable (outils/generes/liens_recherche.html).

Exemples :
    python3 outils/urls_recherche.py
    python3 outils/urls_recherche.py --html
    python3 outils/urls_recherche.py --zone nice
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import quote_plus

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_tracker as T  # noqa: E402

ZONES = {
    "marseille": "Marseille",
    "aix": "Aix-en-Provence",
    "vitrolles": "Vitrolles",
    "etang": "étang de Berre",
    "fos": "Fos-sur-Mer",
    "aubagne": "Aubagne",
    "paca": "Provence-Alpes-Côte d'Azur",
    "13": "Bouches-du-Rhône",
    "nice": "Nice",
}

MOTS_CLES = [
    "alternance commerce international",
    "alternance import export",
    "alternance assistant export",
    "apprentissage assistant import export",
    "alternance ADV export",
    "alternance déclarant en douane",
    "alternance supply chain",
    "alternance achats internationaux",
    "alternance transitaire",
    "alternance agent de transit",
    "alternance développement commercial international",
    "alternance logistique internationale",
]

NAF = {
    "46.19A/B": "Intermédiaires du commerce de gros (négociants, courtiers)",
    "46.39": "Commerce de gros alimentaire non spécialisé",
    "46.38": "Autres commerces de gros alimentaires (produits de la mer, sel, huiles…)",
    "46.71": "Commerce de gros de combustibles et de produits annexes",
    "52.29A": "Messagerie, fret express",
    "52.29B": "Affrètement et organisation des transports (transitaires)",
    "50.20Z": "Transports maritimes et côtiers de fret",
    "46.90": "Commerce de gros non spécialisé (import-export)",
    "10.89Z": "Autres industries alimentaires",
    "20.42Z": "Fabrication de parfums et de produits pour la toilette",
}


def google(q: str) -> str:
    return f"https://www.google.com/search?q={quote_plus(q)}"


def groupes(zone: str) -> list:
    return [
        ("Job boards généralistes", [
            ("Indeed — offres alternance", f"https://fr.indeed.com/jobs?q={quote_plus('alternance commerce international')}&l={quote_plus(zone)}"),
            ("Indeed — import/export", f"https://fr.indeed.com/jobs?q={quote_plus('alternance import export')}&l={quote_plus(zone)}"),
            ("Hellowork", f"https://www.hellowork.com/fr-fr/emploi/recherche.html?k={quote_plus('alternance commerce international')}&l={quote_plus(zone)}"),
            ("Meteojob", f"https://www.meteojob.com/jobs?search={quote_plus('alternance commerce international')}&searchLocation={quote_plus(zone)}"),
            ("Jooble", f"https://fr.jooble.org/emploi-{quote_plus('import-export-alternance')}/{quote_plus(zone)}"),
            ("Jobijoba — alternance assistant import export", "https://www.jobijoba.com/fr/alternance/Assistant+import+export"),
            ("Welcome to the Jungle", f"https://www.welcometothejungle.com/fr/jobs?query={quote_plus('alternance commerce international')}&refinementList%5Boffices.city%5D%5B%5D={quote_plus(zone)}"),
            ("Talent.com", f"https://fr.talent.com/jobs?k={quote_plus('alternance import export')}&l={quote_plus(zone)}"),
            ("Glassdoor", f"https://www.glassdoor.fr/Job/france-{quote_plus(zone)}-alternance-commerce-international-jobs-SRCH_IL.0,6_IN88_KO7,41.htm"),
        ]),
        ("Dispositifs publics", [
            ("La Bonne Alternance — le marché caché (entreprises qui recrutent sans publier)", f"https://labonnealternance.apprentissage.beta.gouv.fr/recherche?job=commerce+international&location={quote_plus(zone)}"),
            ("1jeune1solution — offres d'alternance", f"https://www.1jeune1solution.gouv.fr/alternance?searchTerm={quote_plus('commerce international')}&location={quote_plus(zone)}"),
            ("France Travail — offres en alternance", f"https://candidat.francetravail.fr/offres/recherche?motsCles={quote_plus('alternance commerce international')}&lieux={quote_plus(zone)}"),
            ("Portail de l'alternance (service-public)", "https://www.alternance.emploi.gouv.fr/"),
            ("Walt — l'alternance (communauté)", "https://walt.community/"),
            ("ONISEP — BTS Commerce International en apprentissage", google(f"BTS commerce international apprentissage académie Aix-Marseille site:onisep.fr")),
        ]),
        ("LinkedIn", [
            ("LinkedIn Jobs — alternance commerce international", f"https://www.linkedin.com/jobs/search/?keywords={quote_plus('alternance commerce international')}&location={quote_plus(zone)}"),
            ("LinkedIn Jobs — assistant export", f"https://www.linkedin.com/jobs/search/?keywords={quote_plus('assistant export alternance')}&location={quote_plus(zone)}"),
            ("LinkedIn — personnes « responsable export »", f"https://www.linkedin.com/search/results/people/?keywords={quote_plus('responsable export')}&geoUrn=%5B%22105117694%22%5D"),
            ("LinkedIn — entreprises « transit »", f"https://www.linkedin.com/search/results/companies/?keywords={quote_plus('transit import export')}&location={quote_plus('France')}"),
            ("LinkedIn — posts récents « alternance export »", f"https://www.linkedin.com/search/results/content/?keywords={quote_plus('recherche alternant export')}&sortBy=%22date_posted%22"),
        ]),
        ("Annuaires d'entreprises (pour construire ta propre liste)", [
            ("Europages — import export", f"https://www.europages.fr/entreprises/{quote_plus(zone.lower().replace(' ', '-'))}/entreprise%20import%20export.html"),
            ("Kompass — commerce international", f"https://fr.kompass.com/fr/a/commerce-international-import-export/10/"),
            ("PagesJaunes — commissionnaires transitaires", f"https://www.pagesjaunes.fr/annuaire/{quote_plus(zone.lower().replace(' ', '-'))}-13/commissionnaires-transitaires-auxiliaires-de-transport-international"),
            ("Pappers — recherche d'entreprises par code NAF et ville", "https://www.pappers.fr/entreprise/recherche?q=&cp=&naf=52.29B"),
            ("Societe.com — annuaire", "https://www.societe.com/cgi-bin/search"),
            ("Annuaire des entreprises (data.gouv)", "https://annuaire-entreprises.data.gouv.fr/"),
        ]),
        ("Réseaux et prescripteurs", [
            ("Team France Export — CCI International", "https://www.teamfrance-export.fr/"),
            ("CCI Aix-Marseille-Provence", "https://www.ccimp.com/"),
            ("Marseille Fos Promotion / Union Maritime et Fluviale", "https://www.marseillefos.com/"),
            ("Grand Port Maritime de Marseille — annuaire professionnel", "https://www.marseille-port.fr/"),
            ("Club des entreprises exportatrices / OSCI", "https://www.osci.fr/"),
            ("Chambre de commerce tuniso-française (CCTF)", google("chambre de commerce tuniso-française France")),
        ]),
        ("Recherches ciblées par code NAF (Pappers / societe.com / Google)", [
            (f"NAF {code} — {libelle}", google(f'"{code}" {libelle} {zone} entreprise'))
            for code, libelle in NAF.items()
        ]),
        ("Mots-clés à croiser avec chaque ville (Google / job boards)", [
            (f"{mot} — {zone}", google(f'"{mot}" {zone} entreprise OR offre OR recrutement'))
            for mot in MOTS_CLES[:6]
        ]),
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description="Génère les liens de recherche pré-remplis.")
    ap.add_argument("--zone", default="marseille", choices=sorted(ZONES), help="zone géographique")
    ap.add_argument("--html", action="store_true", help="écrit outils/generes/liens_recherche.html")
    args = ap.parse_args()
    zone = ZONES[args.zone]

    lignes_txt, lignes_html = [], ["<h1>Liens de recherche — " + zone + "</h1>"]
    for titre, liens in groupes(zone):
        lignes_txt.append(f"\n### {titre}")
        lignes_html.append(f"<h2>{titre}</h2><ul>")
        for libelle, url in liens:
            lignes_txt.append(f"  {libelle}\n      {url}")
            lignes_html.append(f'<li><a href="{url}" target="_blank" rel="noopener">{libelle}</a></li>')
        lignes_html.append("</ul>")

    texte = f"Liens de recherche pré-remplis — zone : {zone} — {T.fmt_date(T.aujourdhui())}\n" + "\n".join(lignes_txt)
    print(texte)

    if args.html:
        T.GENERS.mkdir(parents=True, exist_ok=True)
        chemin = T.GENERS / "liens_recherche.html"
        chemin.write_text(
            '<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
            "<title>Liens de recherche</title><style>body{font-family:system-ui,sans-serif;"
            "max-width:900px;margin:2rem auto;padding:0 1rem;line-height:1.5}"
            "h2{margin-top:2rem;border-bottom:1px solid #ddd;padding-bottom:.3rem}"
            "li{margin:.35rem 0}a{color:#0b3d91}</style></head><body>"
            + "\n".join(lignes_html) + "</body></html>", encoding="utf-8")
        print(f"\n✔ Page cliquable écrite : {chemin}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

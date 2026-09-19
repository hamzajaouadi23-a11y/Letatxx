#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generer_cv.py — produit un CV d'une page, en Markdown ET en PDF, à partir de outils/profil.json.

    python3 outils/generer_cv.py
    → outils/generes/cv.md
    → pdf/CV-prenom-nom-alternance-commerce-international.pdf

Tant que profil.json n'est pas rempli, les champs manquants apparaissent entre [crochets
rouges] : c'est voulu, pour que rien ne parte avec un trou.
"""
from __future__ import annotations

import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_tracker as T  # noqa: E402

CLEFS_UTILES = [
    "prenom", "nom", "adresse", "code_postal", "ville", "telephone", "email", "linkedin",
    "age", "nationalite", "titre_sejour", "titre_sejour_validite", "permis",
    "bac_lycee", "bac_annee", "bac_specialites", "bac_mention", "fac_actuelle",
    "ecole", "rythme", "duree_contrat", "date_rentree_ifc", "disponibilite", "zone",
    "niveau_anglais", "niveau_arabe", "niveau_francais", "crm",
    "experiences", "projets", "centres_interet", "points_forts",
]


def champ(prof: dict, cle: str) -> str:
    val = prof.get(cle)
    if isinstance(val, list):
        return ", ".join(str(v) for v in val)
    val = ("" if val is None else str(val)).strip()
    return val


def ou_manquant(prof: dict, cle: str) -> str:
    v = champ(prof, cle)
    return v if v else f"[{cle.upper()} — à compléter]"


def liste_texte(prof: dict, cle: str, puces: str = " - ") -> str:
    val = prof.get(cle) or []
    if isinstance(val, str):
        val = [val]
    return "\n".join(f"{puces}{v}" for v in val if str(v).strip()) or f"{puces}[{cle.upper()} — à compléter]"


def experiences_texte(prof: dict) -> str:
    exps = prof.get("experiences") or []
    blocs = []
    for e in exps:
        if isinstance(e, dict):
            blocs.append(f"{champ(e, 'periode')}   {champ(e, 'poste')} — {champ(e, 'entreprise')}, {champ(e, 'ville')}\n               {champ(e, 'detail')}")
        else:
            blocs.append(str(e))
    return "\n".join(blocs) or "[AUCUNE EXPÉRIENCE — complète la liste 'experiences' dans outils/profil.json]"


def generer_markdown(prof: dict) -> str:
    return f"""# {ou_manquant(prof, 'prenom').upper()} {ou_manquant(prof, 'nom').upper()}

{ou_manquant(prof, 'adresse')} — {ou_manquant(prof, 'code_postal')} {ou_manquant(prof, 'ville')}
{ou_manquant(prof, 'telephone')} · {ou_manquant(prof, 'email')} · {ou_manquant(prof, 'linkedin')}
{ou_manquant(prof, 'age')} ans · nationalité {ou_manquant(prof, 'nationalite')} · titre de séjour valide jusqu'au {ou_manquant(prof, 'titre_sejour_validite')}
Mobilité : {ou_manquant(prof, 'zone')}

---

## RECHERCHE ALTERNANCE — BTS COMMERCE INTERNATIONAL

**Assistant import-export / ADV export / achats internationaux**
{ou_manquant(prof, 'ecole')} — rythme {ou_manquant(prof, 'rythme')} — contrat de {ou_manquant(prof, 'duree_contrat')}
Disponibilité : {ou_manquant(prof, 'disponibilite')}
Français · Arabe ({ou_manquant(prof, 'niveau_arabe')}) · Anglais ({ou_manquant(prof, 'niveau_anglais')})

---

## FORMATION

**{ou_manquant(prof, 'bac_annee')}** — Baccalauréat général, {ou_manquant(prof, 'bac_lycee')} — spécialités {ou_manquant(prof, 'bac_specialites')} — mention {ou_manquant(prof, 'bac_mention')}

**2026-2027** — {ou_manquant(prof, 'fac_actuelle')}

**2026-2027** — {ou_manquant(prof, 'ecole')}
Opérations internationales · relation commerciale interculturelle FR/EN · développement
commercial international · digitalisation de la relation client

---

## COMPÉTENCES

**International** — Incoterms 2020 (EXW, FOB, CIF, DAP, DDP) · liasse documentaire export
(facture commerciale, liste de colisage, connaissement, EUR.1) · bases du dédouanement et de
la TVA à l'import · veille marchés étrangers

**Commercial** — prospection et qualification de fichiers · devis et suivi de commandes ·
relation client multicanal (téléphone, e-mail, messagerie professionnelle)

**Outils** — Excel (tableaux croisés dynamiques, recherches, mise en forme) · Python et SQL
(spécialité NSI : automatisation, traitement de données, requêtes) · {ou_manquant(prof, 'crm')} · Google Workspace

**Langues** — Arabe : {ou_manquant(prof, 'niveau_arabe')} · Français : {ou_manquant(prof, 'niveau_francais')} · Anglais : {ou_manquant(prof, 'niveau_anglais')}

---

## EXPÉRIENCES ET RÉALISATIONS

{experiences_texte(prof)}

**2026** — Projet d'entreprise : négoce de produits tunisiens vers la France
Étude de marché sur l'importation de sel marin et d'huile d'olive tunisiens : identification
de fournisseurs, premiers chiffrages (transport, douane, TVA), réflexion marque et circuit
de distribution CHR / épiceries spécialisées.

---

## PROJETS (spécialité NSI)

{liste_texte(prof, 'projets')}

---

## CENTRES D'INTÉRÊT

{liste_texte(prof, 'centres_interet')}
"""


CSS_CV = """
@page { size: A4; margin: 1.1cm 1.2cm; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 8.6pt; color: #1a1a1a; }
.entete { border-bottom: 1.6pt solid #0b3d91; padding-bottom: 4pt; margin-bottom: 6pt; }
.nom { font-size: 17pt; font-weight: bold; color: #0b3d91; letter-spacing: .5pt; }
.coordonnees { font-size: 8.2pt; color: #333; margin-top: 2pt; }
.titre { background-color: #0b3d91; color: #ffffff; padding: 5pt 7pt; font-size: 10pt; font-weight: bold; margin: 6pt 0 2pt 0; }
.sous-titre { font-size: 8.4pt; color: #16305e; margin-bottom: 6pt; }
h2 { font-size: 9.6pt; color: #0b3d91; text-transform: uppercase; letter-spacing: .6pt;
     border-bottom: .6pt solid #c9d3e8; padding-bottom: 1.5pt; margin: 9pt 0 4pt 0; }
table.ligne { width: 100%; margin-bottom: 3pt; }
td.date { width: 17%; font-weight: bold; color: #16305e; vertical-align: top; font-size: 8.4pt; }
td.contenu { vertical-align: top; }
ul { margin: 2pt 0 2pt 12pt; padding: 0; }
li { margin-bottom: 1.5pt; }
p { margin: 2pt 0; text-align: justify; }
.missing { color: #c0392b; font-weight: bold; }
"""


def generer_html(prof: dict) -> str:
    def esc(cle: str) -> str:
        v = champ(prof, cle)
        if not v:
            return f'<span class="missing">[{cle.upper()} à compléter]</span>'
        return html.escape(v)

    exps = prof.get("experiences") or []
    lignes_exp = []
    for e in exps:
        if isinstance(e, dict):
            lignes_exp.append(
                f'<table class="ligne"><tr><td class="date">{html.escape(champ(e, "periode"))}</td>'
                f'<td class="contenu"><strong>{html.escape(champ(e, "poste"))}</strong> — '
                f'{html.escape(champ(e, "entreprise"))}, {html.escape(champ(e, "ville"))}'
                f'<br>{html.escape(champ(e, "detail"))}</td></tr></table>')
        else:
            lignes_exp.append(f"<p>{html.escape(str(e))}</p>")
    if not lignes_exp:
        lignes_exp = ['<p class="missing">[EXPÉRIENCES à compléter dans outils/profil.json]</p>']

    projets = prof.get("projets") or []
    if isinstance(projets, str):
        projets = [projets]
    interets = prof.get("centres_interet") or []
    if isinstance(interets, str):
        interets = [interets]

    html_projets = "".join(f"<li>{html.escape(str(p))}</li>" for p in projets if str(p).strip())
    if not html_projets:
        html_projets = '<li class="missing">[PROJETS à compléter dans outils/profil.json]</li>'
    html_interets = html.escape(", ".join(str(i) for i in interets if str(i).strip()))
    if not html_interets:
        html_interets = '<span class="missing">[CENTRES D\'INTÉRÊT à compléter dans outils/profil.json]</span>'

    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>CV — alternance BTS Commerce International</title><style>{CSS_CV}</style></head><body>

<div class="entete">
  <div class="nom">{esc('prenom').upper()} {esc('nom').upper()}</div>
  <div class="coordonnees">
    {esc('adresse')} — {esc('code_postal')} {esc('ville')}<br>
    {esc('telephone')} · {esc('email')} · {esc('linkedin')}<br>
    {esc('age')} ans · nationalité {esc('nationalite')} · titre de séjour valide jusqu'au {esc('titre_sejour_validite')} · mobilité : {esc('zone')}
  </div>
</div>

<div class="titre">RECHERCHE ALTERNANCE — BTS COMMERCE INTERNATIONAL (assistant import-export)</div>
<div class="sous-titre">
  {esc('ecole')} — rythme {esc('rythme')} — contrat de {esc('duree_contrat')} — disponibilité : {esc('disponibilite')}<br>
  Français · Arabe ({esc('niveau_arabe')}) · Anglais ({esc('niveau_anglais')}) — intérêt marqué pour les flux France - Maghreb
</div>

<h2>Formation</h2>
<table class="ligne"><tr><td class="date">{esc('bac_annee')}</td><td class="contenu">
  <strong>Baccalauréat général</strong> — {esc('bac_lycee')} — spécialités {esc('bac_specialites')}, mention {esc('bac_mention')}</td></tr></table>
<table class="ligne"><tr><td class="date">2026-2027</td><td class="contenu">
  {esc('fac_actuelle')}</td></tr></table>
<table class="ligne"><tr><td class="date">2026-2028</td><td class="contenu">
  <strong>{esc('ecole')}</strong><br>Opérations internationales · relation commerciale interculturelle en français et en anglais ·
  développement commercial international · digitalisation de la relation client · culture économique, juridique et managériale</td></tr></table>

<h2>Compétences</h2>
<p><strong>International</strong> — Incoterms 2020 (EXW, FOB, CIF, DAP, DDP) · liasse documentaire export
(facture commerciale, liste de colisage, connaissement, EUR.1) · bases du dédouanement et de la TVA à l'import · veille marchés étrangers</p>
<p><strong>Commercial</strong> — prospection et qualification de fichiers · devis et suivi de commandes · relation client multicanal</p>
<p><strong>Outils</strong> — Excel (tableaux croisés dynamiques, recherches, mise en forme) · Python et SQL (spécialité NSI : automatisation et traitement de données) · {esc('crm')} · Google Workspace</p>
<p><strong>Langues</strong> — Arabe : {esc('niveau_arabe')} · Français : {esc('niveau_francais')} · Anglais : {esc('niveau_anglais')}</p>

<h2>Expériences et réalisations</h2>
{''.join(lignes_exp)}
<table class="ligne"><tr><td class="date">2026</td><td class="contenu">
  <strong>Projet d'entreprise — négoce de produits tunisiens vers la France</strong><br>
  Étude de marché sur l'importation de sel marin et d'huile d'olive tunisiens : identification de fournisseurs,
  premiers chiffrages (transport, douane, TVA), réflexion marque et circuit de distribution CHR / épiceries spécialisées.</td></tr></table>

<h2>Projets (spécialité NSI)</h2>
<ul>{html_projets}</ul>

<h2>Centres d'intérêt</h2>
<p>{html_interets}</p>

</body></html>"""


def main() -> int:
    prof = T.profil()
    if not prof:
        print("⚠ outils/profil.json est vide ou illisible : le CV sera généré avec des champs manquants.")

    T.GENERS.mkdir(parents=True, exist_ok=True)
    md = generer_markdown(prof)
    (T.GENERS / "cv.md").write_text(md, encoding="utf-8")
    print(f"✔ Markdown : outils/generes/cv.md")

    html_doc = generer_html(prof)
    (T.GENERS / "cv.html").write_text(html_doc, encoding="utf-8")

    T.DOSSIER.joinpath("pdf").mkdir(parents=True, exist_ok=True)
    slug = T.slug(f"{champ(prof, 'prenom') or 'prenom'}-{champ(prof, 'nom') or 'nom'}")
    sortie = T.DOSSIER / "pdf" / f"CV-{slug}-alternance-commerce-international.pdf"
    try:
        import io
        from xhtml2pdf import pisa
        with sortie.open("wb") as fh:
            res = pisa.CreatePDF(io.BytesIO(html_doc.encode("utf-8")), dest=fh, encoding="utf-8")
        if res.err:
            print(f"✘ {res.err} erreur(s) lors de la génération du PDF")
            return 1
    except ImportError:
        print("✘ xhtml2pdf absent : pip install xhtml2pdf")
        return 1
    print(f"✔ PDF : pdf/{sortie.name}  ({sortie.stat().st_size // 1024} Ko)")

    manquants = [c for c in CLEFS_UTILES if not champ(prof, c)]
    if manquants:
        print(f"\n⚠ {len(manquants)} champ(s) à compléter dans outils/profil.json avant d'envoyer ce CV :")
        print("  " + ", ".join(manquants))
    else:
        print("\n✔ Tous les champs du CV sont renseignés.")
    print("  Rappel : relis-le ligne par ligne et fais-le relire — un CV généré n'est jamais un CV fini.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

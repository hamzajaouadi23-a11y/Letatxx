#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md2pdf.py — convertit les documents Markdown du dossier en PDF prêts à envoyer.

Utilise `markdown` (Markdown → HTML) puis `xhtml2pdf` (HTML → PDF), deux bibliothèques
pures Python déjà installées dans cet environnement.

Exemples :
    python3 outils/md2pdf.py                 # convertit la liste par défaut
    python3 outils/md2pdf.py --tous          # convertit tous les .md du dossier
    python3 outils/md2pdf.py --fichier 01-alternance/cv.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_tracker as T  # noqa: E402

try:
    import markdown
except ImportError:
    markdown = None

PDF = T.DOSSIER / "pdf"

DEFAUT = [
    "00-plan-action.md",
    "01-alternance/cv.md",
    "01-alternance/lettre-motivation.md",
    "01-alternance/emails-candidature.md",
    "01-alternance/argumentaire-entreprise.md",
    "01-alternance/entretien.md",
    "01-alternance/entreprises-cibles.md",
    "01-alternance/pistes-ecoles-et-plan-b.md",
    "02-ifc/candidature-ifc.md",
    "03-amu/annulation-remboursement.md",
    "03-amu/lettre-annulation-amu.md",
    "README.md",
]

CSS = """
@page {
  size: A4;
  margin: 1.6cm 1.5cm 1.8cm 1.5cm;
  @frame footer { -pdf-frame-content: footerContent; bottom: 0.6cm; margin-left: 1.5cm;
                  margin-right: 1.5cm; height: 0.8cm; }
}
body { font-family: Helvetica, Arial, sans-serif; font-size: 9.5pt; color: #1a1a1a; line-height: 1.45; }
h1 { font-size: 16pt; color: #0b3d91; margin-bottom: 4pt; }
h2 { font-size: 12.5pt; color: #0b3d91; margin-top: 14pt; border-bottom: 0.6pt solid #c9d3e8; padding-bottom: 2pt; }
h3 { font-size: 11pt; color: #23407a; margin-top: 10pt; }
p, li { text-align: justify; }
ul, ol { margin-left: 12pt; }
table { width: 100%; margin: 6pt 0; font-size: 8.6pt; }
th { background-color: #eef2fb; color: #16305e; text-align: left; padding: 3pt; border: 0.5pt solid #a9b7d4; }
td { padding: 3pt; border: 0.5pt solid #c9d3e8; vertical-align: top; }
pre { background-color: #f5f6f8; border: 0.5pt solid #d4d8e0; padding: 6pt;
      font-family: Courier, monospace; font-size: 8.2pt; white-space: pre-wrap; }
code { font-family: Courier, monospace; font-size: 8.4pt; background-color: #f0f1f4; }
blockquote { background-color: #fff8e6; border-left: 2.5pt solid #e0a800; padding: 5pt 8pt; margin: 6pt 0; font-size: 9pt; }
hr { border: none; border-top: 0.6pt solid #c9d3e8; margin: 10pt 0; }
a { color: #0b3d91; text-decoration: none; }
.footer { font-size: 7.5pt; color: #7a7a7a; text-align: center; }
"""


SYMBOLES = {
    "⚠": "[!]", "⛔": "[STOP]", "🔥": "[!]", "🎯": "", "👌": "", "💡": "[astuce]",
    "✅": "[OK]", "❌": "[NON]", "☑": "[OK]", "☐": "[ ]", "✓": "OK", "✔": "OK", "✘": "NON",
    "✉": "[mail]", "☎": "[tel]", "→": "->", "←": "<-", "↔": "<->", "⇒": "->",
    "⟦": "[", "⟧": "]", "≤": "<=", "≥": ">=", "≠": "!=", "…": "...",
    "★": "*", "☆": "*", "▪": "-", "•": "-", "‣": "-", "⁃": "-",
    "“": '"', "”": '"', "’": "'", "‘": "'", "–": "-", "—": "-",
    "​": "", "‌": "", "‍": "", "\ufe0f": "",
}


def nettoyer_symboles(texte: str) -> str:
    """Remplace les symboles/emojis non couverts par les polices PDF standard."""
    for cle, val in SYMBOLES.items():
        texte = texte.replace(cle, val)
    # on retire les caractères restants hors latin-1 (emojis, pictogrammes)
    return "".join(c for c in texte if ord(c) < 0x100 or c in "€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ")


def convertir(src: Path, dst: Path) -> bool:
    if markdown is None:
        print("✘ la bibliothèque 'markdown' est absente : pip install markdown")
        return False
    texte = nettoyer_symboles(src.read_text(encoding="utf-8"))
    corps = markdown.markdown(
        texte,
        extensions=["tables", "fenced_code", "sane_lists", "toc", "nl2br"],
        output_format="html5",
    )
    html = (
        '<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
        f"<title>{src.stem}</title><style>{CSS}</style></head><body>"
        f"{corps}"
        '<div id="footerContent" class="footer">'
        f"Dossier de réorientation 2026-2027 · {src.stem} · page <pdf:pagenumber>/<pdf:pagecount>"
        "</div></body></html>"
    )
    try:
        from xhtml2pdf import pisa
    except ImportError:
        print("✘ xhtml2pdf absent : pip install xhtml2pdf")
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("wb") as sortie:
        import io
        resultat = pisa.CreatePDF(io.BytesIO(html.encode("utf-8")), dest=sortie, encoding="utf-8")
    if resultat.err:
        print(f"✘ {src.name} : {resultat.err} erreur(s)")
        return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Convertit les Markdown en PDF.")
    ap.add_argument("--tous", action="store_true", help="tous les .md du dossier (hors outils/)")
    ap.add_argument("--fichier", action="append", default=[], help="chemin relatif à ajouter")
    args = ap.parse_args()

    if args.fichier:
        cibles = [T.DOSSIER / f for f in args.fichier]
    elif args.tous:
        cibles = sorted(p for p in T.DOSSIER.rglob("*.md") if "outils" not in p.parts)
    else:
        cibles = [T.DOSSIER / f for f in DEFAUT]

    PDF.mkdir(parents=True, exist_ok=True)
    ok = 0
    for src in cibles:
        if not src.exists():
            print(f"– ignoré (introuvable) : {src.relative_to(T.DOSSIER)}")
            continue
        dst = PDF / (src.relative_to(T.DOSSIER).as_posix().replace("/", "__").replace(".md", ".pdf"))
        if convertir(src, dst):
            print(f"✔ {dst.relative_to(T.DOSSIER)}  ({dst.stat().st_size // 1024} Ko)")
            ok += 1
    print(f"\n{ok}/{len(cibles)} PDF générés dans reorientation-2026/pdf/")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

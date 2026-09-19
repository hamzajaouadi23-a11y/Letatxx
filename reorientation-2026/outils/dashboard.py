#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dashboard.py — tableau de bord web local de ta recherche d'alternance.

    python3 outils/dashboard.py            # http://0.0.0.0:8080
    PORT=9000 python3 outils/dashboard.py

Fonctions :
  · échéances (AMU, IFC, contrat) avec compte à rebours
  · indicateurs de progression (cibles, envois, relances, entretiens, offres)
  · actions dues aujourd'hui avec le texte exact à copier-coller
  · tableau des 38+ cibles : changement de statut, contact, date de dernière action
  · filtre de recherche instantané

Aucune dépendance : serveur HTTP standard Python. Les données vivent dans outils/tracker.csv.
"""
from __future__ import annotations

import html
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_tracker as T  # noqa: E402
import modeles as M      # noqa: E402
from relances import texte_du_jour  # noqa: E402

CSS = """
:root{--bleu:#0b3d91;--bleuclair:#eef2fb;--rouge:#c0392b;--orange:#d98100;--vert:#1e7e34;--gris:#6b7280}
*{box-sizing:border-box}
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:0;background:#f6f7fb;color:#14181f}
header{background:linear-gradient(120deg,#0b3d91,#1f5fbf);color:#fff;padding:22px 26px}
header h1{margin:0;font-size:21px}
header p{margin:6px 0 0;opacity:.9;font-size:13.5px}
main{max-width:1400px;margin:0 auto;padding:20px}
.grille{display:grid;gap:14px}
.kpis{grid-template-columns:repeat(auto-fit,minmax(140px,1fr))}
.carte{background:#fff;border:1px solid #e2e6ef;border-radius:10px;padding:14px 16px;box-shadow:0 1px 2px rgba(16,24,40,.04)}
.carte .valeur{font-size:26px;font-weight:700;line-height:1.1}
.carte .libelle{font-size:12px;color:var(--gris);margin-top:4px;text-transform:uppercase;letter-spacing:.4px}
.echeances{grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}
.echeance{border-left:4px solid var(--gris)}
.echeance.critique{border-left-color:var(--rouge);background:#fff5f4}
.echeance.proche{border-left-color:var(--orange);background:#fffaf0}
.echeance.ok{border-left-color:var(--vert)}
.echeance .jours{font-size:20px;font-weight:700}
.echeance .quoi{font-size:12.5px;color:#374151;margin-top:3px}
h2{font-size:16px;margin:26px 0 10px;color:#16305e}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #e2e6ef;border-radius:10px;overflow:hidden;font-size:13px}
th{background:var(--bleuclair);text-align:left;padding:8px 10px;font-size:11.5px;text-transform:uppercase;letter-spacing:.4px;color:#16305e;border-bottom:1px solid #d8dfef}
td{padding:8px 10px;border-bottom:1px solid #eef0f6;vertical-align:top}
tr:hover td{background:#fbfcff}
select,input[type=text],input[type=date]{font-size:12.5px;padding:4px 6px;border:1px solid #cfd6e6;border-radius:6px;background:#fff}
.prio1{color:var(--rouge);font-weight:700}.prio2{color:var(--orange);font-weight:600}.prio3{color:var(--gris)}
.badge{display:inline-block;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:600;background:#e8edf7;color:#243a63}
.badge.chaud{background:#ffe3e0;color:#a02c1e}.badge.ok{background:#e2f5e7;color:#16662a}
details{background:#fff;border:1px solid #e2e6ef;border-radius:10px;padding:10px 14px;margin-bottom:8px}
summary{cursor:pointer;font-weight:600;font-size:13.5px}
pre{background:#f7f8fb;border:1px solid #e3e7f0;border-radius:8px;padding:10px;font-size:12px;white-space:pre-wrap;
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace;margin:10px 0 4px}
.action{display:flex;gap:10px;align-items:flex-start;flex-wrap:wrap}
.btn{background:var(--bleu);color:#fff;border:none;border-radius:7px;padding:6px 12px;font-size:12.5px;cursor:pointer;text-decoration:none;display:inline-block}
.btn.petit{padding:3px 8px;font-size:11.5px;background:#4b6bb5}
.btn:hover{filter:brightness(1.1)}
.barre{height:8px;background:#e6e9f2;border-radius:999px;overflow:hidden;margin-top:8px}
.barre>span{display:block;height:100%;background:linear-gradient(90deg,#1e7e34,#5cb85c)}
.note{font-size:12px;color:var(--gris)}
.recherche{width:100%;max-width:420px;padding:8px 12px;font-size:14px}
.entete-ligne{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
code{background:#eef1f7;padding:1px 5px;border-radius:4px;font-size:12px}
.foot{text-align:center;color:var(--gris);font-size:12px;padding:24px}
"""

JS = """
function filtrer(){
  const q=document.getElementById('q').value.toLowerCase();
  document.querySelectorAll('#cibles tbody tr').forEach(tr=>{
    tr.style.display = tr.textContent.toLowerCase().includes(q) ? '' : 'none';
  });
}
async function maj(id, champ, valeur){
  const body=new URLSearchParams(); body.set('id',id); body.set('champ',champ); body.set('valeur',valeur);
  const r=await fetch('/maj',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body});
  if(r.ok && champ==='statut'){ location.reload(); } else if(!r.ok){ alert('Échec de la mise à jour'); }
}
function dater(id){
  const body=new URLSearchParams(); body.set('id',id); body.set('champ','date_envoi');
  body.set('valeur', new Date().toISOString().slice(0,10));
  fetch('/maj',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body}).then(()=>location.reload());
}
function copier(bouton){
  const pre=bouton.parentElement.querySelector('pre');
  navigator.clipboard.writeText(pre.innerText).then(()=>{bouton.textContent='copié ✓';setTimeout(()=>bouton.textContent='copier',1400);});
}
"""


def _esc(v) -> str:
    return html.escape(str(v if v is not None else ""))


def rendu_echeances() -> str:
    cartes = []
    for e in T.echeances():
        j = e["jours"]
        classe = "critique" if j <= 7 else ("proche" if j <= 21 else "ok")
        if j < 0:
            jours, classe = f"⛔ dépassée de {abs(j)} j", "critique"
        elif j == 0:
            jours = "🔥 aujourd'hui"
        else:
            jours = f"dans {j} j"
        cartes.append(
            f'<div class="carte echeance {classe}"><div class="jours">{jours}</div>'
            f'<div class="quoi">{_esc(e["libelle"])}<br><span class="note">{T.fmt_date(e["date"])}</span></div></div>'
        )
    return '<div class="grille echeances">' + "".join(cartes) + "</div>"


def rendu_kpis(lignes, dues) -> str:
    s = T.statistiques(lignes)
    objectif = 100
    pct = min(100, int(100 * s["total"] / objectif))
    cartes = [
        ("Cibles au tracker", s["total"], ""),
        ("À contacter", s.get("a_contacter", 0), ""),
        ("Candidatures envoyées", s.get("envoye", 0) + s.get("contacte", 0), ""),
        ("Relances dues", len(dues), "chaud" if dues else "ok"),
        ("Entretiens", s.get("entretien", 0), "ok" if s.get("entretien") else ""),
        ("Offres / contrats", s.get("offre", 0) + s.get("gagne", 0), "ok" if s.get("offre", 0) + s.get("gagne", 0) else ""),
    ]
    html_c = '<div class="grille kpis">'
    for libelle, valeur, badge in cartes:
        html_c += (f'<div class="carte"><div class="valeur">{valeur}</div>'
                   f'<div class="libelle">{libelle}</div></div>')
    html_c += "</div>"
    html_c += (f'<div class="carte" style="margin-top:14px"><div class="entete-ligne">'
               f'<strong>Progression vers l\'objectif de {objectif} entreprises contactées</strong>'
               f'<span class="badge">{pct} %</span></div>'
               f'<div class="barre"><span style="width:{pct}%"></span></div></div>')
    return html_c


def rendu_actions(dues) -> str:
    if not dues:
        return '<div class="carte">Rien à faire aujourd\'hui : tout est à jour. 👌</div>'
    blocs = []
    for i, d in enumerate(dues, 1):
        l = d["ligne"]
        ctx = T.contexte(l)
        texte = texte_du_jour(l)
        retard = f" · retard {d['retard']} j" if d.get("retard") else ""
        manquants = T.tokens_manquants(texte)
        alerte = ""
        if manquants:
            alerte = ('<div class="note" style="color:#c0392b">Champs à compléter avant envoi : '
                      + ", ".join(f"<code>{m}</code>" for m in manquants)
                      + " → <code>outils/profil.json</code> / colonne <code>contact</code></div>")
        suivante = {"contacte": "envoye", "envoye": "relance1", "relance1": "relance2",
                    "relance2": "sans_reponse", "entretien": "offre"}.get((l.get("statut") or "").strip(), "envoye")
        blocs.append(f"""
<details {'open' if i <= 3 else ''}>
  <summary>{i}. [{_esc(l.get('id'))}] <strong>{_esc(l.get('entreprise'))}</strong>
    <span class="note">{_esc(l.get('ville'))} · priorité {_esc(l.get('priorite'))}</span>
    &nbsp;<span class="badge">{_esc(d['etiquette'])}</span>
    <span class="note">{retard}</span></summary>
  <div class="note" style="margin-top:6px"><strong>Angle :</strong> {_esc(l.get('angle'))}<br>
    <strong>Contact :</strong> {_esc(l.get('contact') or '⟦à identifier⟧')} ·
    <strong>Canal :</strong> {_esc(l.get('email_url') or l.get('canal'))}</div>
  {alerte}
  <div class="action" style="margin-top:8px">
    <button class="btn petit" onclick="copier(this)">copier</button>
    <button class="btn petit" onclick="maj({int(l.get('id') or 0)},'statut','{suivante}')">
      marquer « {_esc(T.STATUT_LABELS.get(suivante, suivante))} »</button>
    <button class="btn petit" onclick="dater({int(l.get('id') or 0)})">dater l'action aujourd'hui</button>
  </div>
  <pre>{_esc(texte)}</pre>
</details>""")
    return "".join(blocs)


def rendu_tableau(lignes) -> str:
    options = "".join(f'<option value="{c}">{lb}</option>' for c, lb in T.STATUTS)
    lignes_html = []
    for l in sorted(lignes, key=lambda x: (str(x.get("priorite") or "9"), str(x.get("entreprise")))):
        due, etiquette, retard = T.prochaine_action(l)
        badge = ('<span class="badge chaud">action due</span>' if due and l.get("statut") not in T.STATUTS_TERMINES
                 else '<span class="badge ok">à jour</span>' if l.get("statut") not in T.STATUTS_TERMINES else "")
        sel = options.replace(f'value="{l.get("statut")}"', f'value="{l.get("statut")}" selected')
        lignes_html.append(f"""<tr>
<td>{_esc(l.get('id'))}</td>
<td><span class="prio{_esc(l.get('priorite'))}">{_esc(l.get('priorite'))}</span></td>
<td><strong>{_esc(l.get('entreprise'))}</strong><div class="note">{_esc(l.get('secteur'))}</div></td>
<td>{_esc(l.get('ville'))}</td>
<td>{_esc(l.get('poste_vise'))}</td>
<td><input type="text" value="{_esc(l.get('contact'))}" placeholder="nom + fonction" style="width:150px"
      onchange="maj({_esc(l.get('id'))},'contact',this.value)"></td>
<td><select onchange="maj({_esc(l.get('id'))},'statut',this.value)">{sel}</select><div style="margin-top:4px">{badge}</div></td>
<td><input type="date" value="{_esc(l.get('date_envoi'))}" onchange="maj({_esc(l.get('id'))},'date_envoi',this.value)">
    <div class="note">{_esc(T.fmt_date(l.get('date_envoi')) or '—')}</div></td>
<td><div class="note">{_esc(etiquette)}</div></td>
<td><a class="btn petit" href="/cible?id={_esc(l.get('id'))}">fiche</a></td>
</tr>""")
    return f"""<table id="cibles"><thead><tr>
<th>#</th><th>Prio</th><th>Entreprise</th><th>Ville</th><th>Poste visé</th><th>Contact</th>
<th>Statut</th><th>Dernière action</th><th>Prochaine étape</th><th></th>
</tr></thead><tbody>{''.join(lignes_html)}</tbody></table>"""


def rendu_fiche(ident: str) -> str:
    lignes = T.charger_lignes()
    l = next((x for x in lignes if str(x.get("id")) == ident), None)
    if not l:
        return "<p>Cible introuvable.</p>"
    ctx = T.contexte(l)
    version = T.version_lettre(l)
    blocs = [("E-mail de candidature", T.remplir(M.EMAIL_CANDIDATURE, ctx)),
             (f"Lettre de motivation (version {version})", T.remplir(M.LETTRES[version], ctx)),
             ("Relance J+4", T.remplir(M.RELANCE_J4, ctx)),
             ("Relance J+10", T.remplir(M.RELANCE_J10, ctx)),
             ("Relance J+20", T.remplir(M.RELANCE_J20, ctx)),
             ("Remerciement après entretien", T.remplir(M.REMERCIEMENT_ENTRETIEN, ctx)),
             ("Fiche d'appel téléphonique", T.remplir(M.NOTES_APPEL, ctx))]
    corps = "".join(
        f'<details><summary>{_esc(t)}</summary><div class="action" style="margin-top:8px">'
        f'<button class="btn petit" onclick="copier(this)">copier</button></div><pre>{_esc(x)}</pre></details>'
        for t, x in blocs)
    return f"""<h2>{_esc(l.get('entreprise'))} — fiche complète</h2>
<div class="carte"><strong>Secteur :</strong> {_esc(l.get('secteur'))} ·
<strong>Ville :</strong> {_esc(l.get('ville'))} · <strong>Taille :</strong> {_esc(l.get('taille'))}<br>
<strong>Poste visé :</strong> {_esc(l.get('poste_vise'))}<br>
<strong>Angle d'attaque :</strong> {_esc(l.get('angle'))}<br>
<strong>Canal :</strong> {_esc(l.get('canal'))} · {_esc(l.get('email_url'))}<br>
<strong>Notes :</strong> {_esc(l.get('notes'))}<br>
<a class="btn" href="/">← retour au tableau de bord</a></div>{corps}"""


def rendu_page(chemin: str, params: dict) -> str:
    lignes = T.charger_lignes()
    dues = T.relances_dues(lignes)
    if chemin == "/cible":
        corps = rendu_fiche((params.get("id") or [""])[0])
    else:
        corps = f"""
<h2>Échéances</h2>{rendu_echeances()}
<h2>Progression</h2>{rendu_kpis(lignes, dues)}
<h2>Actions dues aujourd'hui — {len(dues)}</h2>
<div class="note" style="margin-bottom:8px">Texte généré depuis <code>outils/profil.json</code> +
<code>outils/tracker.csv</code>. Copie, colle, envoie, puis marque l'action comme faite.</div>
{rendu_actions(dues)}
<h2>Toutes les cibles</h2>
<div class="entete-ligne" style="margin-bottom:8px">
  <input id="q" class="recherche" type="text" placeholder="Filtrer (entreprise, ville, secteur…)" onkeyup="filtrer()">
  <span class="note">{len(lignes)} cibles · édition directe, enregistrée dans <code>outils/tracker.csv</code></span>
</div>
{rendu_tableau(lignes)}
<h2>Rappels</h2>
<div class="carte"><ul style="margin:0">
<li><strong>Séquence gagnante :</strong> e-mail + appel + relance à J+4, J+10, J+20. Jamais d'e-mail seul pour une PME.</li>
<li><strong>Objectif de volume :</strong> 100 entreprises contactées avant le 15 octobre.</li>
<li><strong>Ordre des opérations :</strong> admission IFC → entreprise → attestation d'inscription IFC → annulation AMU (avant le 20 octobre).</li>
<li><strong>Ne jamais</strong> démissionner d'AMU avant d'avoir l'écrit de l'IFC.</li>
</ul></div>"""
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Alternance — tableau de bord</title><style>{CSS}</style></head><body>
<header><h1>Recherche d'alternance — BTS Commerce International</h1>
<p>Marseille · Aix-en-Provence · étang de Berre — {_esc(T.fmt_date(T.aujourdhui()))} —
candidatures IFC ouvertes jusqu'à fin octobre 2026</p></header>
<main>{corps}</main>
<div class="foot">Dossier de réorientation 2026-2027 · données locales · <code>outils/tracker.csv</code></div>
<script>{JS}</script></body></html>"""


class Gestionnaire(BaseHTTPRequestHandler):
    def _envoyer(self, contenu: bytes, code: int = 200, tipe: str = "text/html; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", tipe)
        self.send_header("Content-Length", str(len(contenu)))
        self.end_headers()
        self.wfile.write(contenu)

    def log_message(self, fmt, *args):  # silencieux
        pass

    def do_GET(self):
        chemin, _, requete = self.path.partition("?")
        params = parse_qs(requete)
        if chemin in ("/", "/cible"):
            self._envoyer(rendu_page(chemin, params).encode("utf-8"))
        elif chemin == "/api":
            lignes = T.charger_lignes()
            donnees = {"lignes": lignes, "statistiques": T.statistiques(lignes),
                       "echeances": [{**e, "date": T.fmt_date(e["date"])} for e in T.echeances()],
                       "dues": [d["ligne"]["id"] for d in T.relances_dues(lignes)]}
            self._envoyer(json.dumps(donnees, ensure_ascii=False, indent=1).encode("utf-8"),
                          tipe="application/json; charset=utf-8")
        elif chemin == "/favicon.ico":
            self._envoyer(b"", 204)
        else:
            self._envoyer(b"<h1>404</h1>", 404)

    def do_POST(self):
        chemin, _, _ = self.path.partition("?")
        longueur = int(self.headers.get("Content-Length") or 0)
        donnees = parse_qs(self.rfile.read(longueur).decode("utf-8"))
        if chemin != "/maj":
            self._envoyer(b"<h1>404</h1>", 404)
            return
        ident = (donnees.get("id") or [""])[0].strip()
        champ = (donnees.get("champ") or [""])[0].strip()
        valeur = (donnees.get("valeur") or [""])[0].strip()
        autorises = {"statut", "contact", "date_envoi", "priorite", "notes", "prochaine_action", "email_url"}
        if champ not in autorises:
            self._envoyer(json.dumps({"ok": False, "erreur": "champ non autorisé"}).encode(), 400,
                          "application/json; charset=utf-8")
            return
        lignes = T.charger_lignes()
        cible = next((x for x in lignes if str(x.get("id")) == ident), None)
        if cible is None:
            self._envoyer(json.dumps({"ok": False, "erreur": "id inconnu"}).encode(), 404,
                          "application/json; charset=utf-8")
            return
        if champ == "statut" and valeur not in T.STATUT_LABELS:
            self._envoyer(json.dumps({"ok": False, "erreur": "statut inconnu"}).encode(), 400,
                          "application/json; charset=utf-8")
            return
        if champ == "statut" and cible.get("statut") != valeur:
            cible["date_envoi"] = T.aujourdhui().isoformat()
        cible[champ] = valeur
        if champ == "date_envoi":
            cible["prochaine_action"] = ""
        T.enregistrer_lignes(lignes)
        self._envoyer(json.dumps({"ok": True, "id": ident, "champ": champ, "valeur": valeur},
                                 ensure_ascii=False).encode("utf-8"), 200,
                      "application/json; charset=utf-8")


def main() -> int:
    port = int(os.environ.get("PORT") or 8080)
    hote = "0.0.0.0"
    serveur = ThreadingHTTPServer((hote, port), Gestionnaire)
    print(f"Tableau de bord : http://{hote}:{port}  (Ctrl+C pour arrêter)")
    print(f"tracker : {T.TRACKER}")
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêté.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

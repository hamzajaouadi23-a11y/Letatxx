# Outils — comment ça marche

Tout est en Python standard (3.8+). Les deux seules bibliothèques ajoutées sont `markdown` et `xhtml2pdf`, utilisées uniquement pour produire les PDF — le reste fonctionne sans rien installer.

```
outils/
├── tracker.csv              ← LA base de données : tes cibles, contacts, statuts, dates
├── profil.json              ← TON identité (à remplir une fois)
├── config.json              ← dates butoirs (AMU, IFC, contrat)
├── modeles.py               ← textes à trous (e-mails, lettres, relances) — éditables
├── lib_tracker.py           ← moteur commun (lecture CSV, remplissage, calcul des relances)
├── generer_cv.py            ← produit le CV (Markdown + PDF 1 page) depuis profil.json
├── generer_candidatures.py  ← produit 1 dossier par entreprise dans generes/
├── ajouter_cible.py         ← ajoute une entreprise au tracker sans ouvrir le CSV
├── relances.py              ← qui contacter aujourd'hui + texte exact + mise à jour des statuts
├── urls_recherche.py        ← ~50 liens de recherche pré-remplis (job boards, annuaires, LinkedIn)
├── dashboard.py             ← tableau de bord web local (kanban, échéances, copier-coller)
├── md2pdf.py                ← convertit les documents Markdown en PDF
├── run.sh                   ← raccourcis
└── generes/                 ← sortie (régénérable, ignoré par git)
```

> `outils/generes/` n'est **pas versionné** (`.gitignore`) : ce sont des fichiers produits, régénérables en une commande (`bash outils/run.sh all`). Les PDF du dossier, eux, sont versionnés dans `reorientation-2026/pdf/`.

---

## Démarrage en 4 étapes

```bash
cd reorientation-2026

# 1. Remplis ton identité (10 minutes, une seule fois)
#    → ouvre outils/profil.json et complète prenom, nom, telephone, email, langues, expériences

# 2. Génère le CV + toutes les candidatures personnalisées
python3 outils/generer_cv.py && python3 outils/generer_candidatures.py

# 3. Regarde ce que tu dois faire aujourd'hui
python3 outils/relances.py --journee

# 4. Ouvre le tableau de bord
python3 outils/dashboard.py        # puis http://localhost:8080
```

---

## Les commandes utiles au quotidien

| Besoin | Commande |
|---|---|
| Qui dois-je contacter aujourd'hui ? | `python3 outils/relances.py` |
| … avec le texte prêt à coller | `python3 outils/relances.py --texte` |
| Mon plan de prospection du jour | `python3 outils/relances.py --journee` |
| Je viens d'envoyer à la cible 3 | `python3 outils/relances.py --maj 3:envoye` |
| J'ai eu un entretien avec la cible 7 | `python3 outils/relances.py --maj 7:entretien` |
| Plusieurs mises à jour d'un coup | `python3 outils/relances.py --maj 3:envoye --maj 7:entretien` |
| Où en suis-je ? | `python3 outils/relances.py --statistiques` |
| Générer mon CV (Markdown + PDF) | `python3 outils/generer_cv.py` |
| Régénérer tous les textes | `python3 outils/generer_candidatures.py` |
| Seulement les priorités 1 | `python3 outils/generer_candidatures.py --priorite 1` |
| Seulement certaines cibles | `python3 outils/generer_candidatures.py --ids 1,2,5` |
| Ajouter une entreprise au tracker | `python3 outils/ajouter_cible.py --entreprise "X" --ville "Marseille" --angle "…"` |
| Importer une liste d'annuaire | `python3 outils/ajouter_cible.py --import-annuaire ma_liste.csv` |
| Les liens de recherche (page cliquable) | `python3 outils/urls_recherche.py --html` |
| Les PDF du dossier | `python3 outils/md2pdf.py` |
| Tout d'un coup | `bash outils/run.sh all` |

---

## Le cycle de vie d'une cible

```
a_contacter → contacte (appel) → envoye → relance1 → relance2 → entretien → offre → gagne
                    ↘ sans_reponse (clôturé)                    ↘ refuse
```

Délais par défaut (modifiables dans `config.json`) :

| Statut | Prochaine action après |
|---|---|
| `contacte` | 4 jours — envoyer la candidature écrite |
| `envoye` | 4 jours — relance 1 (la plus rentable) |
| `relance1` | 10 jours — relance 2 (apport de valeur) |
| `relance2` | 20 jours — relance 3 (clôture) |
| `entretien` | 3 jours — relance post-entretien |

Quand tu changes le statut (dans le tableau de bord ou avec `--maj`), la **date du jour** est enregistrée comme date de dernière action : le compte à rebours repart tout seul.

---

## Ajouter une cible

**Option A — en ligne de commande (recommandé) :**
```bash
python3 outils/ajouter_cible.py \
  --entreprise "Transit Express Méditerranée" \
  --ville "Marseille 2e" --secteur "Transit / douane" --taille PME \
  --poste "assistant import-export" --priorite 2 \
  --angle "PME de transit maritime, renfort sur la saisie des dossiers export" \
  --canal "Téléphone + e-mail" --url "https://exemple.fr/contact"
```
Les doublons sont détectés automatiquement (même nom d'entreprise).

**Option B — importer une liste d'annuaire** (Europages, Kompass, PagesJaunes exportés en CSV) :
```bash
python3 outils/ajouter_cible.py --import-annuaire ma_liste.csv
```
Le CSV doit contenir au minimum une colonne `entreprise` ; les autres colonnes reconnues
(`ville`, `secteur`, `taille`, `poste_vise`, `angle`, `canal`, `contact`, `email_url`,
`priorite`, `notes`) sont reprises telles quelles.

**Option C — éditer `outils/tracker.csv`** dans un tableur (LibreOffice, Excel, Google Sheets) :
attention à ne pas casser l'ordre des colonnes ni les guillemets autour des champs contenant des virgules.

---

## Ce que les outils ne font pas (volontairement)

- **Ils n'envoient pas les e-mails à ta place.** Envoyer 100 e-mails depuis un script te ferait blacklister et, surtout, te priverait du seul élément qui fait la différence : la ligne personnalisée. L'automatisation prépare, toi tu décides et tu appuies sur envoyer.
- **Ils ne devinent pas les adresses e-mail.** Un champ `⟦à compléter⟧` reste visible tant que tu ne l'as pas renseigné : c'est voulu.
- **Ils n'aspirent pas les job boards.** Le sandbox n'a pas d'accès Internet et ces sites bloquent l'aspiration automatique ; à la place, `urls_recherche.py` te livre des recherches déjà formulées.
- **Ils ne remplacent pas un conseil juridique** sur le titre de séjour ou le remboursement AMU : ils te donnent les bons textes, les bonnes dates et les bonnes questions à poser aux bons interlocuteurs.

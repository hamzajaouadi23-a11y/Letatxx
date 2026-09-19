# Letatxx

Dépôt de travail personnel.

## 📌 Dossier en cours : réorientation 2026-2027

**[→ `reorientation-2026/`](reorientation-2026/README.md)** — passage de la Licence 1 Économie-Gestion (Aix-Marseille Université, FEG) au **BTS Commerce International en alternance** (IFC Marseille), avec pour priorité immédiate la **recherche d'une entreprise d'accueil** sur Marseille / Aix-en-Provence / étang de Berre.

Le dossier contient :

- le **plan d'action daté** du 19 septembre au 31 décembre 2026 ;
- le **kit complet de prospection** : 38 entreprises cibles, CV, 4 lettres de motivation, e-mails et séquence de relances, argumentaire financier pour l'employeur, préparation d'entretien (20 questions/réponses + kit technique import-export) ;
- les **démarches IFC** (candidature, attestation d'inscription) et **AMU** (annulation d'inscription + remboursement des 2 902 €, critère applicable, délais, pièges) ;
- des **outils automatisés** (Python, sans dépendance lourde) : tableau de bord web, générateur de candidatures et de CV, gestion des relances, liens de recherche pré-remplis, export PDF.

```bash
cd reorientation-2026
bash outils/run.sh all          # génère CV, candidatures, liens et PDF
python3 outils/dashboard.py     # tableau de bord → http://localhost:8080
```

Détails : [`reorientation-2026/README.md`](reorientation-2026/README.md) et [`reorientation-2026/outils/README.md`](reorientation-2026/outils/README.md).

## 📄 Autre fichier du dépôt

- `COURSWB.pdf` — document PDF chiffré par mot de passe (non lisible en l'état).

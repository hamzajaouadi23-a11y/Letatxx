# Dossier de réorientation 2026-2027 — Licence Éco-Gestion (AMU) → BTS Commerce International en alternance

> Généré le **samedi 19 septembre 2026**. Priorité assumée : **trouver l'entreprise d'accueil**.
> Zone de recherche : **Marseille + Aix-en-Provence + étang de Berre (Vitrolles, Marignane, Rognac, Les Pennes-Mirabeau, Aubagne, Gémenos, Fos)**.

---

## ⏱ Les 3 dates qui commandent tout

| Date | Événement | Conséquence si ratée |
|---|---|---|
| **~24-26 octobre 2026** | Fin de la fenêtre AMU pour demander l'annulation d'inscription **+** remboursement des 2 902 € | Aucune seconde chance sur l'année : la demande est rejetée hors délai |
| **Fin octobre 2026** | Fin des candidatures IFC (dans la limite des places disponibles) | Plus de place en BTS CI → année perdue ou plan B |
| **Avant les partiels de décembre** | Il ne faut **pas** avoir validé d'UE à AMU | L'annulation d'inscription AMU devient impossible si des UE sont validées |

**Ordre des opérations imposé par ces dates :**
`Admission IFC` → `entreprise d'accueil` → `attestation d'inscription IFC` → `demande d'annulation + remboursement AMU (avant le 24 oct.)`.

Ne **jamais** démissionner d'AMU avant d'avoir l'écrit de l'IFC en main.

---

## 📁 Contenu du dossier

| Fichier | À quoi ça sert |
|---|---|
| `00-plan-action.md` | Calendrier daté semaine par semaine, du 21/09 au 31/12, avec les volumes d'actions à tenir |
| `01-alternance/entreprises-cibles.md` | 38 cibles réelles classées par priorité + méthode pour en trouver 100 |
| `01-alternance/cv.md` | CV une page, orienté import-export (avec les emplacements à compléter) |
| `01-alternance/lettre-motivation.md` | 3 lettres selon le type d'entreprise (transitaire / négoce PME / grand groupe) |
| `01-alternance/emails-candidature.md` | E-mails courts, objets, relances J+4 / J+10 / J+20, LinkedIn, script téléphonique |
| `01-alternance/argumentaire-entreprise.md` | One-pager à envoyer aux PME : « ce que je vous coûte vraiment » (chiffres 2026) |
| `01-alternance/entretien.md` | Pitch 60 s, 20 questions/réponses, kit technique (Incoterms, liasse, EUR.1 Tunisie, douane) |
| `01-alternance/pistes-ecoles-et-plan-b.md` | Plan B et C : autres écoles qui placent en entreprise, BTS public, démarrage sans employeur |
| `02-ifc/candidature-ifc.md` | Checklist du dossier IFC + e-mail prêt à envoyer à `marseille@ifc.fr` + 10 questions à poser |
| `03-amu/annulation-remboursement.md` | Procédure exacte, le critère qui te concerne, les 4 pièges, les pièces |
| `03-amu/lettre-annulation-amu.md` | Lettre/courriel de demande d'annulation + remboursement, prêt à personnaliser |
| `outils/` | **Automatisation** : tableau de bord, générateur de candidatures, relances, URLs de recherche, conversion PDF |
| `pdf/` | Versions PDF générées, prêtes à envoyer |

---

## 🤖 Ce qui est automatisé pour toi

Tout est dans `outils/` — aucune dépendance à installer, Python 3 standard + `markdown`/`xhtml2pdf` (déjà installés).

| Commande | Effet |
|---|---|
| `bash outils/run.sh all` | Génère le CV, les 38 candidatures personnalisées, les liens de recherche, tous les PDF, et liste les relances dues |
| `python3 outils/dashboard.py` | **Tableau de bord web** (échéances, actions du jour, kanban éditable, textes à copier) — lancé en preview sur le port 8080 |
| `python3 outils/generer_cv.py` | Produit ton **CV 1 page en PDF** (et en Markdown) depuis `profil.json`, avec les champs manquants signalés en rouge |
| `python3 outils/generer_candidatures.py` | Remplit les modèles depuis `profil.json` + `tracker.csv` → pour chaque entreprise : e-mail, lettre (version adaptée au secteur), fiche d'appel, 3 relances, remerciement |
| `python3 outils/relances.py --journee` | Affiche **qui contacter aujourd'hui** + le plan de la journée (10 appels, 10 e-mails, 5 actions réseau) |
| `python3 outils/relances.py --maj 3:envoye` | Met à jour un statut ; le compte à rebours de relance repart automatiquement |
| `python3 outils/ajouter_cible.py` | Ajoute une entreprise au tracker (ou importe un CSV d'annuaire) sans ouvrir le fichier |
| `python3 outils/urls_recherche.py --html` | ~50 liens de recherche **pré-remplis** (Indeed, Hellowork, La Bonne Alternance, 1jeune1solution, LinkedIn, Europages, Kompass, PagesJaunes, Pappers par code NAF…) |
| `python3 outils/md2pdf.py` | Convertit les documents Markdown en PDF dans `pdf/` |

**Le seul travail manuel qu'il te reste :**
1. remplir `outils/profil.json` une fois (identité, contact, langues, expériences) — **les textes générés affichent `⟦TOKEN⟧` tant que ce n'est pas fait** ;
2. identifier les contacts (colonne `contact` du tracker) et envoyer les textes générés ;
3. mettre à jour les statuts dans le tableau de bord au fil de l'eau.

---

## ⚠️ Deux points à régler dans les 48 h (avant d'envoyer 40 candidatures)

1. **Ton titre de séjour.** En tant que ressortissant tunisien hors UE, l'apprentissage est en principe conditionné à **un an de présence préalable en France** avec un titre « étudiant » (art. R5221-7 du Code du travail, décret n° 2021-360), et l'employeur doit vérifier le titre auprès de la préfecture **au moins 2 jours ouvrables avant l'embauche** (art. L5221-8, R5221-41/42). Selon les cas, une **autorisation de travail** doit être demandée par l'employeur sur l'ANEF. → **Fais confirmer par écrit ta situation par l'IFC (service relations entreprises) et par le bureau des étudiants internationaux d'AMU.** C'est un point qui bloque parfois les employeurs : autant l'avoir éclairci et pouvoir répondre en une phrase en entretien.
2. **Ne pas démissionner d'AMU trop tôt.** Tant que tu es sous titre « étudiant », ton inscription universitaire est un élément de ton dossier de renouvellement. On n'annule qu'avec l'attestation IFC + le contrat signé (ou une réponse écrite de la préfecture).

Détails et formulations prêtes à l'emploi : `00-plan-action.md` (semaine 1) et `01-alternance/entretien.md` (question « ton statut »).

---

## 🎯 Le raisonnement en une phrase

Tu n'as pas besoin d'**une** entreprise qui t'adore : tu as besoin de **100 contacts** envoyés en 10 jours, dont sortiront statistiquement 5 à 10 entretiens et 1 contrat — et tu as trois arguments massue : **tu ne coûtes presque rien** (4 500 € d'aide employeur la 1re année pour une PME, salaire net 802,82 €/mois), **tu parles arabe et tu connais le marché tunisien** (rare et directement monnayable sur les flux France-Maghreb), et **tu es disponible 3 jours par semaine dès maintenant**.

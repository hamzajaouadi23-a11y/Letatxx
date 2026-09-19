# Plan d'action daté — du samedi 19 septembre au 31 décembre 2026

Règle du jeu : **la recherche d'alternance est une activité commerciale**. Tu appliques à toi-même ce que tu veux apprendre : ciblage, volume, personnalisation, relance. Personne ne répond à 1 candidature, tout le monde répond à 100 candidatures relancées 3 fois.

**Objectif chiffré :** 100 entreprises contactées avant le 15 octobre → 5 à 10 entretiens → 1 contrat signé avant le 15 décembre.

---

## Semaine 0 — aujourd'hui, samedi 19 septembre (2 h)

- [ ] Remplir `outils/profil.json` (identité, contact, langues, expériences réelles). **Ne rien inventer.**
- [ ] Ouvrir le tableau de bord : `python3 outils/dashboard.py` → vérifier les 38 cibles.
- [ ] Scanner et ranger dans un dossier `pieces/` : pièce d'identité, titre de séjour, bulletins de 1re et Terminale, attestation de réussite au bac, reçu de paiement AMU (2 902 €), RIB à ton nom, certificat de scolarité AMU 2026-2027.
- [ ] **Deux appels/e-mails bloquants** (voir scripts dans `02-ifc/candidature-ifc.md`) :
  - [ ] IFC Marseille (`marseille@ifc.fr` + téléphone) : date exacte de rentrée, rythme, places restantes en BTS CI, accompagnement au placement, **liste des offres d'alternance de leurs entreprises partenaires**, et la question titre de séjour/autorisation de travail.
  - [ ] Scolarité FEG AMU (campus Colbert) : retirer le **formulaire de demande d'annulation d'inscription administrative**, demander la **date limite exacte 2026** pour le dépôt, et confirmer le critère « acceptation tardive dans un autre établissement hors EP » + la retenue de 23 €.
- [ ] Créer une adresse e-mail dédiée si la tienne n'est pas sobre : `prenom.nom.pro@gmail.com`.
- [ ] Mettre à jour LinkedIn : photo, titre « Recherche alternance BTS Commerce International — Marseille/Aix (dispo 3 j/semaine) », section « à l'écoute d'opportunités » activée.

---

## Semaine 1 — lundi 21 → dimanche 27 septembre

**Objectif : dossier IFC déposé + 25 candidatures envoyées.**

- [ ] **Lundi** : compléter et envoyer le dossier de candidature IFC (formulaire PDF du site + pièces) à `marseille@ifc.fr`. Objet : `Candidature BTS Commerce International en alternance – rentrée 2026 – [Prénom Nom]`.
- [ ] **Lundi** : envoyer l'e-mail de demande d'**attestation d'admission/d'inscription** (modèle dans `02-ifc/candidature-ifc.md`) — c'est la pièce qui débloquera ton remboursement AMU.
- [ ] **Mardi** : finaliser le CV (1 page, `01-alternance/cv.md`) → PDF. Faire relire par ton père (il recrute des commerciaux : son avis vaut de l'or).
- [ ] **Mercredi** : lancer le générateur `python3 outils/generer_candidatures.py` → envoyer **10 candidatures** aux priorités 1 du tracker (Marée Albe, M&M, Seatrans, Cofrapex, Pernod Ricard, GD France, CEVA, Mathez, ITEM, SOMEXPORT).
- [ ] **Jeudi** : **10 appels téléphoniques** aux PME (les TPE/PME ne lisent pas les e-mails : elles décrochent le téléphone). Script dans `01-alternance/emails-candidature.md`.
- [ ] **Vendredi** : 5 candidatures supplémentaires + 10 connexions LinkedIn avec messages personnels.
- [ ] **Week-end** : alimenter le tracker à 60 cibles (méthode annuaires dans `01-alternance/entreprises-cibles.md` : Europages, Kompass, PagesJaunes, annuaire CCI, membres de Marseille Fos Promotion).

> 💡 **Piste n°1 à traiter dès lundi : Marée Albe.** C'est le chemin le plus court vers un contrat : la société existe, fait déjà de l'import-export franco-tunisien, et ton père en est directeur commercial. Deux options : (a) Marée Albe devient ton entreprise d'accueil ; (b) ton père t'ouvre 5 portes de son réseau (transitaires, négociants, importateurs). Les deux se tentent en parallèle — voir le pitch interne dans `01-alternance/argumentaire-entreprise.md`.

---

## Semaine 2 — lundi 28 septembre → dimanche 4 octobre

**Objectif : 50 candidatures cumulées, 1er entretien IFC, 1res relances.**

- [ ] 15 nouvelles candidatures (priorité 2 : grands comptes et transitaires de la Joliette, Vitrolles, Fos).
- [ ] Passer l'entretien d'admission IFC (préparé avec `01-alternance/entretien.md`).
- [ ] **Relance J+4** sur toutes les candidatures de la semaine 1 : `python3 outils/relances.py` te donne la liste et le texte.
- [ ] Deux actions réseau :
  - [ ] Prendre contact avec **Team France Export** / **CCI Aix-Marseille-Provence** : demander la liste des PME exportatrices du 13 et les événements à venir.
  - [ ] Demander à ton père une **introduction écrite** (LinkedIn ou e-mail) vers 3 transitaires ou négociants qu'il connaît.
- [ ] Candidater en parallèle à 2 ou 3 écoles qui placent elles-mêmes en entreprise (`01-alternance/pistes-ecoles-et-plan-b.md`) — pas pour y aller, mais pour **accéder à leurs offres d'alternance partenaires**.

---

## Semaine 3 — lundi 5 → dimanche 11 octobre

**Objectif : 75 candidatures, relance J+10, première décision.**

- [ ] 15 nouvelles candidatures (priorité 3 + CHR/épiceries fines importatrices).
- [ ] Relance **J+10** sur la semaine 1, **J+4** sur la semaine 2.
- [ ] Relance téléphonique sur les 10 PME les plus prometteuses.
- [ ] **Point de décision à faire le dimanche 11 octobre** :
  - Au moins 2 entretiens obtenus ? → continuer sur la même ligne.
  - Zéro réponse après 75 candidatures ? → le problème est le CV ou la cible, pas le volume. Refaire le CV avec ton père, et basculer sur les écoles à placement garanti + les secteurs en tension (transit/douane, où les employeurs cherchent activement).

---

## Semaine 4 — lundi 12 → dimanche 18 octobre

**Objectif : 100 candidatures, relance J+20, et sécuriser l'AMU.**

- [ ] Relance finale **J+20** (texte « je clôture mes recherches » : c'est souvent celle qui déclenche une réponse).
- [ ] **Si admission IFC obtenue et entreprise en vue** : demander l'**attestation d'inscription** à l'IFC **cette semaine** (elle est indispensable au dossier AMU).
- [ ] Préparer le dossier AMU complet (`03-amu/`) sans le déposer encore.
- [ ] Vérifier auprès de la préfecture/ANEF ou du bureau des étudiants internationaux AMU l'effet du changement d'établissement sur ton titre de séjour.

---

## Semaine 5 — lundi 19 → dimanche 25 octobre  ⚠️ SEMAINE CRITIQUE

- [ ] **Avant le 24 octobre : déposer la demande d'annulation d'inscription + remboursement AMU** (délai constaté : 24/10 en composante, 26/10 selon la FAQ AMU — viser le 20 octobre pour ne pas dépendre d'une interprétation).
  - Dépôt **physique** en scolarité FEG + **e-mail** en parallèle, avec accusé.
  - Pièces : formulaire, attestation d'inscription IFC, reçu de paiement, RIB, courrier de motivation (modèle fourni).
- [ ] Dernière salve de candidatures IFC : confirmer par écrit que ton dossier est bien retenu.

---

## Semaines 6 à 10 — 26 octobre → 30 novembre

**Objectif : signer le contrat d'apprentissage.**

- [ ] Entretenir le rythme : 10 nouvelles candidatures/semaine + relances. Le volume ne s'arrête pas quand les cours commencent.
- [ ] Si tu as commencé la formation sans employeur : tu peux être en **statut de stagiaire de la formation professionnelle** pendant **3 mois maximum** (art. L6222-12-1 du Code du travail) — demande à l'IFC de confirmer ce dispositif par écrit et qui paie la formation pendant cette période.
- [ ] Dès qu'une entreprise dit oui : faire remplir le **Cerfa contrat d'apprentissage**, le transmettre à l'IFC/CFA, dépôt auprès de l'OPCO, et vérification du titre de séjour par l'employeur (2 jours ouvrables avant l'embauche).

---

## Décembre

- [ ] Signature du contrat au plus tard (fenêtre des 3 mois après le début du cycle de formation).
- [ ] Vérifier que le remboursement AMU est bien instruit (relance agence comptable / scolarité).
- [ ] Mettre en place ta routine d'alternance : 2 jours IFC, 3 jours entreprise.
- [ ] **Seulement ensuite** : ouvrir le chantier du projet entrepreneurial Tunisie ↔ France (segment reporté à ta demande).

---

## Le tableau de bord des volumes (à tenir)

| Semaine | Nouvelles candidatures | Cumul | Appels | Relances envoyées | Entretiens obtenus |
|---|---|---|---|---|---|
| S1 | 25 | 25 | 10 | 0 | 0 |
| S2 | 15 | 40 | 10 | 25 | ? |
| S3 | 15 | 55 | 10 | 40 | ? |
| S4 | 20 | 75 | 10 | 55 | ? |
| S5 | 25 | 100 | 15 | 75 | ? |

# CV — alternance BTS Commerce International

**Format cible : 1 page, PDF, nom de fichier `CV-Prenom-NOM-alternance-commerce-international.pdf`.**
Les champs entre `{{ }}` sont remplis automatiquement depuis `outils/profil.json` par `generer_candidatures.py` (ou à compléter à la main — 10 minutes).

---

## Ce que doit dire ton CV en 6 secondes

Un recruteur en transit/négoce lit trois choses : **es-tu disponible**, **parles-tu anglais (et quoi d'autre)**, **as-tu la tête bien faite**. Ton profil coche une case rare : **arabe + connaissance du marché tunisien**. C'est ton argument n°1 sur les flux France-Maghreb — il doit apparaître **dans le titre**, pas enterré en bas.

---

```
{{PRENOM}} {{NOM}}
{{ADRESSE}} — {{CODE_POSTAL}} {{VILLE}}
{{TELEPHONE}} · {{EMAIL}} · {{LINKEDIN}}
18 ans · nationalité tunisienne · titre de séjour « étudiant » valide jusqu'au {{TITRE_SEJOUR_VALIDITE}}
Permis {{PERMIS}} · Mobilité : Marseille, Aix-en-Provence, étang de Berre

———————————————————————————————————————————————
RECHERCHE ALTERNANCE — BTS COMMERCE INTERNATIONAL (IFC Marseille)
Assistant import-export / ADV export / achats internationaux
Rythme 2 jours en formation · 3 jours en entreprise — disponible immédiatement
Français · Arabe (courant) · Anglais ({{NIVEAU_ANGLAIS}}) — fort intérêt pour les flux France ↔ Maghreb
———————————————————————————————————————————————

FORMATION
2026-2027  BTS Commerce International — IFC Marseille (diplôme d'État, niveau 5, 120 ECTS)
           Opérations internationales · relation commerciale interculturelle FR/EN ·
           développement commercial international · digitalisation de la relation client
2026-2027  Licence 1 Économie-Gestion — Aix-Marseille Université (FEG) — réorientation confirmée
           vers le commerce international (projet professionnel aligné sur l'import-export)
2026       Baccalauréat général — {{BAC_LYCEE}} — spécialités Mathématiques & NSI — mention {{BAC_MENTION}}

COMPÉTENCES
International  Incoterms 2020 (EXW, FOB, CIF, DAP, DDP) · liasse documentaire export (facture
               commerciale, liste de colisage, connaissement, EUR.1) · bases du dédouanement et
               de la TVA à l'import · veille marchés étrangers
Commercial     Prospection et qualification de fichiers · devis et suivi de commandes ·
               relation client multicanal (téléphone, e-mail, WhatsApp professionnel)
Outils         Excel (tableaux croisés dynamiques, recherches, mise en forme) · Python et SQL
               (spécialité NSI : scripts d'automatisation, traitement de données, requêtes) ·
               Canva · CRM ({{CRM}}) · outils Google Workspace
Langues        Arabe : courant (lu, écrit, parlé — atout direct sur le Maghreb)
               Français : courant (scolarité française)
               Anglais : {{NIVEAU_ANGLAIS}} — pratique commerciale écrite et orale

EXPÉRIENCES ET RÉALISATIONS
{{EXP_DATE}}   {{EXP_POSTE}} — {{EXP_ENTREPRISE}}, {{EXP_VILLE}}
               {{EXP_DETAIL}}

2026           Projet d'entreprise — négoce de produits tunisiens vers la France
               Étude de marché sur l'importation de sel marin et d'huile d'olive tunisiens :
               identification de fournisseurs, premiers chiffrages (transport, douane, TVA),
               réflexion marque et circuit de distribution CHR/épiceries spécialisées.

PROJETS (spécialité NSI)
{{PROJET_1}}
{{PROJET_2}}

CENTRES D'INTÉRÊT
{{CENTRES_INTERET}}
```

> Les champs `{{EXP_*}}` correspondent à la liste `experiences` de `outils/profil.json` : remplis-les là-bas, puis recopie-les dans ton CV final. Le CV n'est pas généré automatiquement — c'est volontaire : c'est le document que tu dois relire et soigner ligne par ligne.

---

## Les 7 réglages qui changent tout

1. **Le titre est une promesse, pas un intitulé.** « Recherche alternance — BTS Commerce International — assistant import-export, disponible immédiatement, 3 j/semaine » répond à la seule question du recruteur : *est-ce que je peux l'utiliser ?*
2. **Arabe en deuxième langue, jamais en dernier.** Sur un flux Marseille → Radès/Sfax, c'est un avantage concurrentiel, pas une ligne de couleur.
3. **NSI = ton avantage caché.** Excel + Python + SQL, dans une PME de transit ou de négoce, ça veut dire : « je peux automatiser vos tableaux de suivi, vos fichiers clients, vos comparatifs de fret ». Peu de candidats en BTS CI savent le faire. Écris-le, démontre-le en entretien (voir `entretien.md`).
4. **Ne pas cacher la L1 Éco-Gestion, la raconter.** Une ligne, une raison, zéro justification. Formulation validée : « réorientation confirmée vers le commerce international ». Jamais « je n'aimais pas la fac ».
5. **La ligne « projet d'entreprise » est un atout, à condition d'être rassurante.** Elle prouve la motivation et la compréhension du métier. En entretien, tu dis clairement : *« mon projet est à 3-5 ans ; aujourd'hui je veux apprendre le métier chez vous et m'y investir deux ans »*. Sans cette phrase, certains employeurs craignent que tu partes.
6. **Les expériences : même petites, elles comptent.** Baby-sitting, caisse, aide dans l'entreprise familiale, bénévolat, job d'été, aide à la traduction : tout ce qui montre contact client, rigueur, argent manié. Ne laisse pas la section vide — sinon mets uniquement la ligne « projet d'entreprise ».
7. **Un seul PDF, un seul nom de fichier.** `CV-Prenom-NOM-alternance-commerce-international.pdf`. Jamais `cv_final_v3.pdf`.

---

## À bannir

- La photo d'identité mal cadrée ou la photo de vacances recadrée.
- Les jauges de compétences (●●●●○) : personne ne sait ce qu'elles signifient.
- « Dynamique, motivé, sérieux » sans preuve : remplace par un chiffre ou un fait.
- Plus d'une page.
- Les fautes : fais relire par deux personnes, dont une qui n'est pas de ta famille.

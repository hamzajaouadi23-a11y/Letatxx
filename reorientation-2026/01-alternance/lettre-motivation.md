# Lettres de motivation — 3 versions selon le type d'entreprise

Toutes les versions sont remplies automatiquement (`{{ENTREPRISE}}`, `{{ANGLE}}`, `{{POSTE}}` (poste visé mis en forme), `{{VILLE}}`) par `python3 outils/generer_candidatures.py` à partir du tracker. Une lettre = **20 lignes maximum**. Personne ne lit plus.

---

## Version A — Transitaire / commissionnaire en douane / logistique internationale
*(M&M, Seatrans, Mathez Freight, Prolog, Transtime, Grospiron, DSV, Seko Bansard, CEVA, Geodis, K+N, DHL, MSC, Maersk, CMA CGM, GPMM)*

```
Objet : Candidature alternance BTS Commerce International — {{POSTE}} (3 jours/semaine)

Madame, Monsieur,

{{ENTREPRISE}} organise des flux entre la France et le Maghreb, et c'est précisément le
métier que je veux apprendre : {{ANGLE}}.

Je prépare le BTS Commerce International à l'IFC de Marseille (diplôme d'État, niveau 5,
120 ECTS), sur un rythme de 2 jours en formation et 3 jours en entreprise. Je suis donc
disponible 3 jours par semaine, immédiatement, pour une durée de 24 mois.

Baccalauréat général spécialités mathématiques et NSI en 2026, je suis à l'aise avec les
chiffres, les procédures et les outils : Excel (tableaux croisés dynamiques), Python et
SQL, ce qui me permet d'automatiser des suivis de dossiers, des tableaux de bord ou des
fichiers clients dès les premières semaines.

Je parle arabe couramment, en plus du français et de l'anglais ({{NIVEAU_ANGLAIS}}). Sur
des dossiers Tunisie / Maghreb, c'est un avantage concret : je peux lire un document,
comprendre un interlocuteur et lever une ambiguïté sans intermédiaire.

Mon projet professionnel est le négoce international entre la Tunisie et la France. Je ne
cherche pas un poste d'attente : je cherche une maison où apprendre sérieusement la liasse
documentaire, le dédouanement, les Incoterms et la relation client export, et où m'investir
deux ans.

Je serais heureux de vous rencontrer pour vous exposer ma motivation, et je me permets de
vous rappeler en début de semaine prochaine.

Je vous prie d'agréer, Madame, Monsieur, mes salutations distinguées.

{{PRENOM}} {{NOM}} — {{TELEPHONE}} — {{EMAIL}}
```

---

## Version B — PME de négoce / import-export agro ou produits de grande consommation
*(ITEM, SOMEXPORT, Equateur Fruits, SML Import Export, Sayviv'on Trading, WEMADE, LPT, GFS Logistics, GD France)*

```
Objet : Alternance 24 mois — {{POSTE}} — BTS Commerce International (dispo 3 j/semaine)

Madame, Monsieur,

{{ANGLE}} : c'est exactement le périmètre sur lequel je souhaite me former pendant deux ans.

Je prépare le BTS Commerce International à l'IFC de Marseille (diplôme d'État, 120 ECTS),
rythme 2 jours formation / 3 jours entreprise. Concrètement, je suis présent chez vous
3 jours par semaine, toute l'année, pour 24 mois.

Ce que je peux prendre en charge rapidement : saisie et suivi des commandes, préparation
des offres et des devis, mise à jour des fichiers clients et fournisseurs, tableaux de
suivi Excel, veille tarifaire, relances, préparation des documents commerciaux. Ma
spécialité NSI au bac (mathématiques, informatique) me permet d'automatiser les fichiers
et les reportings plutôt que de les ressaisir.

Je parle arabe couramment, français et anglais ({{NIVEAU_ANGLAIS}}). Je m'intéresse au
négoce de produits méditerranéens entre la Tunisie et la France, ce qui suppose de
comprendre le sourcing, les conditions de vente, la logistique et la conformité : votre
activité est pour moi un terrain d'apprentissage idéal.

Je vous appelle dans les prochains jours pour savoir si un échange est possible.

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}} — {{EMAIL}}
```

---

## Version C — Grand groupe / industriel avec activité export
*(Pernod Ricard, Boisset, Corania, Bpifrance, CMA CGM, Decathlon United…)*

```
Objet : Contrat d'apprentissage 24 mois — {{POSTE_VISE}} (BTS Commerce International, IFC Marseille)

Madame, Monsieur,

Votre offre d'alternance {{POSTE_VISE}} à {{VILLE}} correspond au métier que je prépare :
{{ANGLE}}.

Admis au BTS Commerce International de l'IFC Marseille (diplôme d'État, niveau 5, 120 ECTS),
je suis en recherche d'un contrat d'apprentissage de 24 mois, sur un rythme de 2 jours en
formation et 3 jours en entreprise, avec une disponibilité immédiate.

Mon parcours : baccalauréat général 2026 spécialités mathématiques et NSI, première année
de licence Économie-Gestion à Aix-Marseille Université, réorientée vers le commerce
international pour aligner ma formation sur un projet professionnel clair — le négoce et
la distribution entre la France et la Tunisie.

Apports concrets : rigueur chiffrée (Excel, statistiques de base), automatisation de
reportings (Python, SQL), anglais professionnel ({{NIVEAU_ANGLAIS}}) et arabe courant,
atout sur les marchés méditerranéens. Je suis à l'aise dans les environnements exigeants
et je préfère les responsabilités progressives aux postes d'observation.

Je reste à votre disposition pour un entretien, en présentiel ou en visioconférence.

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}} — {{EMAIL}} — {{LINKEDIN}}
```

---

## Version D — Le cas particulier Marée Albe (piste n°1)

Ici, le destinataire est ton père : la lettre est inutile, **le pitch interne est décisif** (voir `argumentaire-entreprise.md`). En revanche, si tu passes par un associé, un dirigeant ou le service RH de Marée Albe, utilise cette trame :

```
Objet : Proposition — alternance BTS Commerce International sur le périmètre export (3 j/semaine)

Madame, Monsieur,

Je prépare le BTS Commerce International à l'IFC de Marseille et je cherche une entreprise
d'accueil pour un contrat d'apprentissage de 24 mois, à raison de 3 jours par semaine en
entreprise.

Plutôt qu'une candidature générale, je vous propose un périmètre précis : l'administration
des ventes export et le développement commercial France/Maghreb — suivi des commandes et
des expéditions, liasse documentaire, relation transitaires, mise à jour des tarifs et des
fiches clients, prospection de comptes CHR et grossistes, tableaux de bord.

Le dispositif coûte très peu à l'entreprise : la formation est prise en charge par l'OPCO
et l'embauche d'un apprenti de niveau bac+2 ouvre droit à une aide de 4 500 € maximum la
première année pour une entreprise de moins de 250 salariés (décret n° 2026-168).

Je connais déjà le produit, le marché tunisien et les interlocuteurs. Je suis opérationnel
sur les bases dès la première semaine, et je parle arabe couramment.

Je vous propose 20 minutes d'échange cette semaine pour cadrer les missions et vérifier
la faisabilité administrative.

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
```

---

## Les 5 règles d'or (valables pour toutes les versions)

1. **Première phrase = l'entreprise, pas toi.** Prouve que tu as regardé leur activité.
2. **Deuxième paragraphe = la logistique.** Rythme, durée, disponibilité. C'est ce qui rassure et c'est ce qui manque dans 80 % des candidatures.
3. **Un chiffre ou un fait par compétence.** « Excel » ne vaut rien ; « je construis des tableaux croisés dynamiques » vaut quelque chose.
4. **Tu annonces ta relance.** « Je vous appelle en début de semaine prochaine » — ça double le taux de réponse et ça t'oblige à relancer.
5. **Signature complète avec téléphone.** Un recruteur qui doit chercher ton numéro ne t'appelle pas.

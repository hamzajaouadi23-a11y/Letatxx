# Entreprises cibles — Marseille, Aix-en-Provence, étang de Berre

La liste vivante est dans **`outils/tracker.csv`** (38 cibles pré-remplies) et s'affiche dans le tableau de bord : `python3 outils/dashboard.py`.
Ce document explique **comment la compléter jusqu'à 100 entreprises** et **comment trouver le bon contact**.

---

## 1. La carte des zones à couvrir

| Zone | Ce qu'on y trouve | Priorité |
|---|---|---|
| **Marseille 2e — La Joliette / Euroméditerranée** | Siège CMA CGM, Maersk France, Grospiron, Seko Bansard, Transtime, MSC, armateurs, commissionnaires | ★★★ |
| **Marseille 7e / 14e / 15e** | Prolog, DSV, transitaires, zones d'activité nord | ★★★ |
| **Vitrolles / Marignane / Les Pennes-Mirabeau** | CEVA Logistics, Cofrapex, Corania, logistique aéroportuaire, zones industrielles | ★★★ |
| **Aix-en-Provence / Les Milles / Rousset** | GD France, PME tech et distribution, Galileo/ESARC (écoles partenaires) | ★★ |
| **Fos-sur-Mer / Port-de-Bouc / Martigues** | Grand port, terminaux, vracs, logistique lourde, douane | ★★ (trajet long) |
| **Aubagne / Gémenos** | PME agro, M2S Formation, industrie | ★★ |
| **Salon-de-Provence / Miramas** | logistique, transport | ★ (2e vague) |

**Critère de choix n°1 : le temps de trajet.** Tu seras sur site 3 jours par semaine pendant 24 mois. Une cible à 25 minutes vaut mieux qu'une cible prestigieuse à 1 h 15. Vérifie le trajet **réel aux heures de pointe** avant de candidater.

---

## 2. Les 4 familles de cibles (et l'angle d'attaque de chacune)

### A. Transitaires, commissionnaires en transport et en douane — **ta meilleure famille**
Ils vivent de l'import-export, recrutent en permanence sur des fonctions ADV/transit/douane, et la réforme des formalités (depuis avril 2026, sur plusieurs ports, les négociants doivent mandater un représentant en douane enregistré) met leurs services sous tension.
*Angle :* « Je parle arabe, je suis rigoureux sur le documentaire, et je veux apprendre le dédouanement. »
*Cibles :* Militzer & Münch France, Seatrans, Mathez Freight, Prolog, Transtime, Grospiron, Seko Bansard, DSV, Geodis, DB Schenker, Kuehne+Nagel, DHL Global Forwarding, CEVA, MSC, Maersk, CMA CGM, Méditerranée Transit International, GFS Logistics.

### B. PME de négoce et d'import-export produits — **le cœur de ton futur métier**
Petites équipes = missions complètes, contact direct avec le dirigeant, visibilité sur toute la chaîne (sourçage → prix → transport → douane → vente).
*Angle :* « Je peux prendre l'ADV, les devis, la relance client et les tableaux de suivi, et je comprends le négoce Méditerranée. »
*Cibles :* ITEM, SOMEXPORT, Equateur Fruits, SML Import Export, Sayviv'on Trading, WEMADE, LPT Logistique International, GD France, OSR Sourcing.

### C. Industriels et marques avec service export — **les plus formateurs**
Un vrai service ADV export, des process, de l'anglais quotidien, un réseau.
*Cibles :* Pernod Ricard France (Marseille), Boisset (Marseille), Corania (Les Pennes-Mirabeau, cosmétiques export), Société Ricard, et tout industriel PACA qui vend hors de France.

### D. Écosystème et prescripteurs — **pas des employeurs, des multiplicateurs**
*Team France Export*, *CCI Aix-Marseille-Provence*, *Marseille Fos Promotion / Union Maritime et Fluviale* (l'annuaire des membres est une mine de cibles), *Club export / réseaux d'entreprises*, *conseillers France Travail spécialisés alternance*.
*Angle :* « Je ne viens pas postuler, je viens demander 5 noms d'entreprises qui cherchent un alternant export. »

---

## 3. La méthode « 100 entreprises en 3 jours »

### Jour 1 — construire la liste (3 h)
1. **Europages** et **Kompass** : recherche « import export » + ville Marseille / Aix / Vitrolles → exporter 40 noms.
2. **PagesJaunes** : catégorie « commissionnaires transitaires auxiliaires de transport international » → 20 noms (cette catégorie est un gisement sous-utilisé).
3. **Annuaire des membres de Marseille Fos Promotion** et de la **CCI AMP** → 20 noms.
4. **societe.com / pappers.fr** : recherche par code NAF — `46.19A/B` (intermédiaires du commerce), `46.39` (commerce de gros alimentaire non spécialisé), `52.29A/B` (messagerie, fret, affrètement), `46.71` (commerce de gros de combustibles… inclut les huiles), `10.89` (autres industries alimentaires), `46.38` (autres commerces de gros alimentaires, dont produits de la mer et sel).
5. **LinkedIn** : recherche entreprises « import », « export », « négoce », « transit », « international trade » + localisation Bouches-du-Rhône.

### Jour 2 — trouver le bon contact (3 h)
Pour chaque entreprise, cherche dans cet ordre :
1. **LinkedIn** → personnes avec les intitulés : `responsable export`, `responsable ADV`, `supply chain manager`, `directeur logistique`, `acheteur`, `directeur général` (en PME de moins de 20 salariés, c'est **toujours** le dirigeant qu'il faut contacter).
2. **Site web** → pages « Contact », « Recrutement », mentions légales (l'adresse e-mail du dirigeant y apparaît parfois), formulaire.
3. **Téléphone** → appeler le standard et demander le nom du responsable du service concerné. C'est la méthode la plus rapide et la plus efficace en PME.
4. **Deviner l'e-mail avec vérification** : les schémas `prenom.nom@societe.fr`, `p.nom@`, `initiale.nom@`, `contact@`, `rh@`, `export@`, `adv@`. *À n'utiliser qu'en dernier recours, et à tester : un e-mail qui rebondit te fait perdre du temps et de la crédibilité.*

### Jour 3 — envoyer et appeler (3 h)
- 50 e-mails personnalisés (générateur : `python3 outils/generer_candidatures.py`).
- 20 appels téléphoniques (script : `emails-candidature.md`).
- Mise à jour du tracker au fil de l'eau, sinon tu perds le fil en 48 heures.

---

## 4. Comment prioriser

Note chaque cible de 1 à 5 sur trois critères, et traite d'abord celles dont le total est le plus élevé :

| Critère | Question |
|---|---|
| **Pertinence métier** | Vais-je toucher à l'import-export réel (documents, douane, fret, négociation) ou à de la saisie ? |
| **Probabilité** | Petite structure qui recrute déjà ? Secteur en tension ? Contact déjà chaud (réseau de mon père) ? |
| **Faisabilité** | Trajet ≤ 35 min ? Rythme compatible ? Statut administratif simple pour l'employeur ? |

**Règle pratique :** une PME de 10 personnes avec un dirigeant joignable au téléphone bat une multinationale avec un portail de recrutement. Vise **70 % de PME**.

---

## 5. Les cibles « réseau » à activer en premier (ta rente immatérielle)

Ton père est directeur commercial d'une société franco-tunisienne. C'est un actif que 99 % des candidats de 18 ans n'ont pas. Trois demandes concrètes à lui faire **cette semaine**, par écrit pour qu'il puisse transférer :

1. **Marée Albe comme entreprise d'accueil** — voir le pitch interne dans `argumentaire-entreprise.md`.
2. **Cinq introductions nominatives** : transitaires avec qui il travaille, importateurs clients, confrères négociants, agents en Tunisie ayant une structure en France. Un message transféré (« je te recommande mon fils, il cherche une alternance export, il est sérieux et parle arabe ») se convertit en entretien dans 50 % des cas.
3. **Le réseau tunisien en France** : chambres de commerce franco-tunisiennes, associations d'entrepreneurs tunisiens en PACA, importateurs de produits tunisiens (dattes, huile d'olive, harissa, produits de la mer). Ces structures cherchent souvent des profils bilingues franco-arabes et sont peu sollicitées par les étudiants en BTS.

> ⚠️ Un conseil de prudence : ne demande jamais à ton père d'appeler quelqu'un sans lui donner **un support écrit à transférer** (3 lignes + ton CV). Il doit pouvoir recommander sans se mouiller, et toi apparaître comme un professionnel, pas comme « le fils de ».

---

## 6. Le suivi

- Tous les soirs, 5 minutes : mets à jour les statuts dans le tableau de bord.
- Chaque matin : `python3 outils/relances.py` → la liste des relances dues et le texte à coller.
- Chaque dimanche : regarde le tableau de bord, compte les entretiens obtenus, et corrige ce qui ne fonctionne pas (CV, cible, volume, canal).

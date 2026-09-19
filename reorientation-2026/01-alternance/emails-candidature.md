# E-mails, relances, LinkedIn, téléphone — tout le kit de prospection

Règle n°1 : **l'e-mail seul ne suffit jamais pour une PME.** La séquence gagnante, c'est e-mail + appel + relance e-mail. C'est exactement de la prospection commerciale — tu l'apprends en la faisant.

---

## 1. L'e-mail de candidature (court, 7 lignes)

Les recruteurs de PME lisent sur leur téléphone, entre deux dossiers. Long = pas lu.

```
Objet : Alternance BTS Commerce International — {{POSTE}} — dispo 3 j/semaine

Bonjour,

Je prépare le BTS Commerce International à l'IFC de Marseille (2 jours formation /
3 jours entreprise, contrat de 24 mois) et je cherche une entreprise d'accueil
{{ANGLE_COURT}}.

Je suis disponible immédiatement, 3 jours par semaine, sur {{VILLE}}.
Bac général maths/NSI 2026, arabe courant, anglais {{NIVEAU_ANGLAIS}}, à l'aise
avec Excel, Python et SQL.

CV en pièce jointe. Je vous appelle {{JOUR_APPEL}} pour savoir si un échange est possible.

Merci de votre temps,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
```

**5 objets qui fonctionnent** (à alterner, jamais deux fois le même à la même boîte) :
- `Alternance BTS Commerce International — assistant import-export — dispo 3 j/semaine`
- `Apprenti export FR/AR/EN — 3 jours par semaine chez vous dès maintenant`
- `Candidature alternance 24 mois — {{ENTREPRISE}} / commerce international`
- `Votre service export : un alternant à 428 €/mois net d'aide la 1re année`  *(à réserver aux PME, cf. `argumentaire-entreprise.md`)*
- `Flux France-Tunisie : alternant BTS CI, arabe courant, dispo immédiate`

---

## 2. Les relances (le vrai levier : +50 % de réponses)

### Relance J+4 — la plus importante
```
Objet : Re: Alternance BTS Commerce International — {{POSTE}}

Bonjour,

Je me permets de revenir vers vous sur ma candidature du {{DATE_ENVOI}} pour une
alternance en commerce international.

Un élément utile si votre activité connaît des pics : je suis disponible
3 jours par semaine dès maintenant, et je parle arabe couramment, ce qui peut
servir directement sur des dossiers Maghreb.

Avez-vous besoin d'un complément (CV détaillé, références, entretien en visio) ?

Merci,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
```

### Relance J+10 — l'apport de valeur
```
Objet : Re: Alternance BTS Commerce International

Bonjour,

Sans retour de votre part, je suppose que le moment n'est pas idéal. Je me permets
quand même de vous laisser une information qui pourrait vous être utile :
{{APPORT}} — par exemple, un point sur l'évolution des formalités douanières vers
le Maghreb, ou un mini-tableau de suivi que j'ai construit pour un cas similaire.

Si une alternance de 24 mois peut vous intéresser plus tard dans l'année, gardez
mon contact : je reste disponible.

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
```

### Relance J+20 — la clôture (déclenche souvent la réponse)
```
Objet : Je clôture mes recherches — dernière nouvelle

Bonjour,

Je finalise mon choix d'entreprise d'accueil pour mon BTS Commerce International.
Je vous laisse la priorité jusqu'à {{DATE_LIMITE}}, car votre activité
{{ANGLE_COURT}} correspond exactement à ce que je cherche.

Sans retour de votre part à cette date, je considérerai que ce n'est pas possible
cette année et je n'insisterai plus.

Merci pour votre lecture,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
```

> ⚠️ N'envoie la relance J+20 que si tu es prêt à la tenir. Une menace de clôture non tenue te grille.

---

## 3. Le script téléphonique (10 PME par jour, 45 minutes)

**Objectif de l'appel : obtenir un nom et un rendez-vous. Pas raconter ta vie.**

```
« Bonjour, {{PRENOM}} {{NOM}}, je cherche la personne qui s'occupe du service
export / des achats / de la logistique. C'est possible de me la passer ? »

→ Si on te la passe :
« Bonjour Monsieur/Madame X, je vous appelle 30 secondes : je prépare un BTS
Commerce International à Marseille, en alternance, 3 jours par semaine en
entreprise pendant 24 mois. Je parle arabe couramment et je cherche une maison
comme la vôtre pour apprendre l'import-export. Est-ce que vous prenez des
alternants cette année ? »

→ Si OUI :
« Parfait. Quel est le meilleur moment pour un entretien de 20 minutes, cette
semaine ou la suivante ? Je peux venir sur site. »

→ Si NON / PAS MAINTENANT :
« Je comprends. Puis-je vous envoyer mon CV pour que vous l'ayez sous la main si
un besoin apparaît ? Quelle est votre adresse e-mail directe ? »
   [noter le nom + l'e-mail direct = victoire]

→ Si on te renvoie vers les RH / un portail :
« Je le ferai, mais pour être utile : sur quels sujets votre équipe est-elle le
plus en tension en ce moment — les dossiers export, la saisie, les relances
clients ? » [réponse = matière pour personnaliser l'e-mail suivant]
```

**Après chaque appel (2 minutes) :** ajouter le contact dans `outils/tracker.csv`, statuer, programmer la relance. `python3 outils/relances.py` te redonne la liste chaque matin.

---

## 4. LinkedIn

### Le titre (à changer aujourd'hui)
```
Alternance BTS Commerce International (IFC Marseille) — Assistant import-export |
FR · AR · EN | Disponible 3 jours/semaine dès maintenant | Marseille · Aix · Vitrolles
```

### La note de connexion (limite : 300 caractères)
```
Bonjour {{PRENOM_CONTACT}}, je prépare un BTS Commerce International à Marseille
et je m'intéresse aux flux France-Maghreb de {{ENTREPRISE}}. Puis-je vous suivre
et, si l'occasion se présente, vous poser deux questions sur votre métier ?
Merci !
```

### Le message après acceptation
```
Merci pour votre retour {{PRENOM_CONTACT}}. Deux questions très courtes :
1) Votre service prend-il des alternants, ou l'a-t-il déjà fait ?
2) Sinon, qui me conseilleriez-vous de contacter chez {{ENTREPRISE}} ?
Je cherche un contrat de 24 mois, 3 jours par semaine en entreprise, dispo
immédiate. Arabe courant, anglais {{NIVEAU_ANGLAIS}}, Excel/Python.
```

### Les 8 recherches LinkedIn à enregistrer (alertes hebdomadaires)
1. `alternance import export Marseille`
2. `alternance commerce international Aix-en-Provence`
3. `assistant export alternance Bouches-du-Rhône`
4. `apprenti supply chain Vitrolles`
5. `déclarant en douane alternance`
6. `assistant achats internationaux alternance PACA`
7. `transitaire Marseille` (personnes → pour identifier les responsables d'exploitation)
8. `responsable export` + filtre « Tunisie » ou « Maghreb »

---

## 5. Les 4 erreurs qui font échouer une prospection

| Erreur | Correction |
|---|---|
| Envoyer 10 candidatures puis attendre | Le volume minimum est de 100 contacts en 4 semaines |
| Copier-coller le même texte partout | Une ligne personnalisée sur l'activité de l'entreprise suffit — mais elle est obligatoire |
| Ne pas relancer | 60 % des réponses arrivent après la 1re relance |
| Candidater uniquement aux offres publiées | Le marché caché (candidatures spontanées) représente la majorité des alternances en PME : c'est justement ce que fait `La Bonne Alternance` |

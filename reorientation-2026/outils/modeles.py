#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
modeles.py — textes à trous utilisés par generer_candidatures.py et relances.py.

Édite librement ces modèles : tout ce qui est entre {{ }} est remplacé par les valeurs
de outils/profil.json et de la ligne correspondante dans outils/tracker.csv.
Ce qui n'est pas renseigné apparaît sous la forme ⟦TOKEN⟧ pour être immanquable.
"""

EMAIL_CANDIDATURE = """Objet : Alternance BTS Commerce International — {{POSTE}} — dispo 3 j/semaine

Bonjour,

Je prépare le BTS Commerce International à l'IFC de Marseille (2 jours formation /
3 jours entreprise, contrat de 24 mois) et je cherche une entreprise d'accueil :
{{ANGLE_COURT}}.

Je suis disponible immédiatement, 3 jours par semaine, sur {{VILLE}}.
Bac général maths/NSI 2026, arabe courant, anglais {{NIVEAU_ANGLAIS}}, à l'aise
avec Excel, Python et SQL.

CV en pièce jointe. Je vous appelle {{JOUR_APPEL}} pour savoir si un échange est possible.

Merci de votre temps,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
"""

RELANCE_J4 = """Objet : Re: Alternance BTS Commerce International — {{POSTE}}

Bonjour,

Je me permets de revenir vers vous sur ma candidature du {{DATE_ENVOI_LUE}} pour une
alternance en commerce international.

Un élément utile : je suis disponible 3 jours par semaine dès maintenant, et je parle
arabe couramment, ce qui peut servir directement sur des dossiers Maghreb.

Avez-vous besoin d'un complément (CV détaillé, références, entretien en visio) ?

Merci,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
"""

RELANCE_J10 = """Objet : Re: Alternance BTS Commerce International

Bonjour,

Sans retour de votre part, je suppose que le moment n'est pas idéal. Je vous laisse
néanmoins une information qui peut vous être utile : {{APPORT}}.

Si une alternance de 24 mois en commerce international peut vous intéresser plus tard
dans l'année, gardez mon contact : je reste disponible et je prospecte sur
{{ZONE}}.

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
"""

RELANCE_J20 = """Objet : Je clôture mes recherches — dernière nouvelle

Bonjour,

Je finalise mon choix d'entreprise d'accueil pour mon BTS Commerce International.
Je vous laisse la priorité jusqu'au {{DATE_LIMITE}}, car votre activité
({{ANGLE_COURT}}) correspond exactement à ce que je cherche.

Sans retour de votre part à cette date, je considérerai que ce n'est pas possible
cette année et je n'insisterai plus.

Merci pour votre lecture,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
"""

RELANCE_APRES_ENTRETIEN = """Objet : Suite à notre échange — alternance BTS Commerce International

Bonjour {{PRENOM_CONTACT}},

Je reviens vers vous après notre échange du {{DATE_ENVOI_LUE}} concernant une alternance
de 24 mois sur un périmètre {{ANGLE_COURT}}.

Je vous confirme ma disponibilité : 3 jours par semaine en entreprise, immédiatement,
et mon engagement sur la durée complète du BTS. Si votre décision n'est pas encore prise,
je reste à votre disposition pour un second échange, une mise en relation avec l'IFC sur
les aspects administratifs, ou un test de niveau d'anglais.

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
"""

REMERCIEMENT_ENTRETIEN = """Objet : Merci pour notre échange — alternance BTS Commerce International

Bonjour {{PRENOM_CONTACT}},

Merci pour le temps que vous m'avez accordé aujourd'hui. J'ai particulièrement retenu
{{POINT_PRECIS}} : c'est exactement le type de missions sur lesquelles je veux progresser.

Je confirme ma disponibilité : 3 jours par semaine, dès que le contrat est signé, pour
24 mois. Je reste à votre disposition pour tout complément (références, test d'anglais,
échange avec l'IFC sur le calendrier).

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}}
"""

LETTRE_A = """Objet : Candidature alternance BTS Commerce International — {{POSTE}} (3 jours/semaine)

Madame, Monsieur,

{{ENTREPRISE}} organise des flux entre la France et l'international, et c'est précisément
le métier que je veux apprendre : {{ANGLE_COURT}}.

Je prépare le BTS Commerce International à l'IFC de Marseille (diplôme d'État, niveau 5,
120 ECTS), sur un rythme de 2 jours en formation et 3 jours en entreprise. Je suis donc
disponible 3 jours par semaine, immédiatement, pour une durée de 24 mois.

Baccalauréat général spécialités mathématiques et NSI en 2026, je suis à l'aise avec les
chiffres, les procédures et les outils : Excel (tableaux croisés dynamiques), Python et
SQL, ce qui me permet d'automatiser des suivis de dossiers, des tableaux de bord ou des
fichiers clients dès les premières semaines.

Je parle arabe couramment, en plus du français et de l'anglais ({{NIVEAU_ANGLAIS}}). Sur
des dossiers Maghreb, c'est un avantage concret : je peux lire un document, comprendre un
interlocuteur et lever une ambiguïté sans intermédiaire.

Mon projet professionnel est le négoce international entre la Tunisie et la France. Je ne
cherche pas un poste d'attente : je cherche une maison où apprendre sérieusement la liasse
documentaire, le dédouanement, les Incoterms et la relation client export, et où m'investir
deux ans.

Je serais heureux de vous rencontrer pour vous exposer ma motivation, et je me permets de
vous rappeler {{JOUR_APPEL}}.

Je vous prie d'agréer, Madame, Monsieur, mes salutations distinguées.

{{PRENOM}} {{NOM}} — {{TELEPHONE}} — {{EMAIL}}
"""

LETTRE_B = """Objet : Alternance 24 mois — {{POSTE}} — BTS Commerce International (dispo 3 j/semaine)

Madame, Monsieur,

{{ANGLE_COURT}} : c'est exactement le périmètre sur lequel je souhaite me former pendant
deux ans.

Je prépare le BTS Commerce International à l'IFC de Marseille (diplôme d'État, 120 ECTS),
rythme 2 jours formation / 3 jours entreprise. Concrètement, je suis présent chez vous
3 jours par semaine, toute l'année, pendant 24 mois.

Ce que je peux prendre en charge rapidement : saisie et suivi des commandes, préparation
des offres et des devis, mise à jour des fichiers clients et fournisseurs, tableaux de
suivi Excel, veille tarifaire, relances, préparation des documents commerciaux. Ma
spécialité NSI au baccalauréat (mathématiques, informatique) me permet d'automatiser les
fichiers et les reportings plutôt que de les ressaisir.

Je parle arabe couramment, français et anglais ({{NIVEAU_ANGLAIS}}). Je m'intéresse au
négoce de produits méditerranéens entre la Tunisie et la France, ce qui suppose de
comprendre le sourçage, les conditions de vente, la logistique et la conformité : votre
activité est pour moi un terrain d'apprentissage idéal.

Je vous appelle dans les prochains jours pour savoir si un échange est possible.

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}} — {{EMAIL}}
"""

LETTRE_C = """Objet : Contrat d'apprentissage 24 mois — {{POSTE_VISE}} (BTS Commerce International, IFC Marseille)

Madame, Monsieur,

Votre activité d'alternance {{POSTE_VISE}} à {{VILLE}} correspond au métier que je prépare :
{{ANGLE_COURT}}.

Admis au BTS Commerce International de l'IFC Marseille (diplôme d'État, niveau 5, 120 ECTS),
je recherche un contrat d'apprentissage de 24 mois, sur un rythme de 2 jours en formation
et 3 jours en entreprise, avec une disponibilité immédiate.

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
"""

LETTRE_D = """Objet : Proposition — alternance BTS Commerce International sur le périmètre export (3 j/semaine)

Madame, Monsieur,

Je prépare le BTS Commerce International à l'IFC de Marseille et je cherche une entreprise
d'accueil pour un contrat d'apprentissage de 24 mois, à raison de 3 jours par semaine en
entreprise.

Plutôt qu'une candidature générale, je vous propose un périmètre précis : l'administration
des ventes export et le développement commercial France/Maghreb — suivi des commandes et
des expéditions, liasse documentaire, relation transitaires, mise à jour des tarifs et des
fiches clients, prospection de comptes CHR et grossistes, tableaux de bord.

Le dispositif coûte très peu à l'entreprise : la formation est prise en charge par l'OPCO
et l'embauche d'un apprenti préparant un diplôme de niveau 5 ouvre droit à une aide pouvant
atteindre 4 500 € la première année pour une entreprise de moins de 250 salariés (décret
n° 2026-168).

Je connais déjà le produit, le marché tunisien et les interlocuteurs. Je suis opérationnel
sur les bases dès la première semaine, et je parle arabe couramment.

Je vous propose 20 minutes d'échange cette semaine pour cadrer les missions et vérifier la
faisabilité administrative.

Bien cordialement,
{{PRENOM}} {{NOM}} — {{TELEPHONE}} — {{EMAIL}}
"""

LETTRES = {"A": LETTRE_A, "B": LETTRE_B, "C": LETTRE_C, "D": LETTRE_D}

NOTES_APPEL = """Fiche d'appel — {{ENTREPRISE}} ({{VILLE}})
------------------------------------------------------------
Avant d'appeler : {{ANGLE}}
Canal : {{CANAL}} — {{EMAIL_URL}}
Contact : {{CONTACT}}

Phrase d'ouverture :
  « Bonjour, {{PRENOM}} {{NOM}}, je cherche la personne qui s'occupe du service
  export / des achats / de la logistique. C'est possible de me la passer ? »

Pitch 20 secondes :
  « Je prépare un BTS Commerce International à Marseille, en alternance, 3 jours par
  semaine en entreprise pendant 24 mois. Je parle arabe couramment et je cherche une
  maison comme la vôtre pour apprendre l'import-export. Est-ce que vous prenez des
  alternants cette année ? »

À noter pendant l'appel :
  Nom de l'interlocuteur : ............................................
  Fonction : ..........................................................
  E-mail direct : .....................................................
  Réponse (oui / non / plus tard) : ...................................
  Sujet de tension évoqué : ...........................................
  Prochaine étape + date : ............................................
"""

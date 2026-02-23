# CARRON, LEOTE, WACQUIEZ

# Industrialisation des tests – Examen

Projet de test automatisé (Selenium) sur le formulaire de création de compte Wikimedia.

## Ce qui a été fait

- **Test du formulaire de création de compte** sur `auth.wikimedia.org` (page Spécial:Créer un compte).
- Le script remplit les champs : nom d’utilisateur, mot de passe, confirmation du mot de passe, email.
- **Validation** : on vérifie que les valeurs saisies sont bien présentes dans chaque input (via `get_attribute("value")`), sans soumettre le formulaire.

### Choix de ne pas soumettre le formulaire (captcha)

L’envoi du formulaire déclenche un **captcha** sur la page Wikimedia. Pour éviter la complexité et les limites liées au captcha en automatisation, nous avons **volontairement décidé de ne pas faire le submit** :

- Le test ne clique pas sur le bouton de création de compte.
- Il se contente de remplir les champs et de valider que les données sont bien inscrites dans les inputs.
- Ainsi, le test reste fiable, reproductible et ne dépend pas du captcha.

## Prérequis

- Python 3
- Chrome (pour Selenium / ChromeDriver)

## Installation

Créer un environnement virtuel et installer les dépendances :

```bash
python3 -m venv venv
source venv/bin/activate          # sur Windows : venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Exécuter le test

Avec le venv activé :

```bash
python ex1.py
```

En cas de succès, le script affiche :  
`Tous les champs ont été correctement remplis.`  
et se termine sans erreur. Si une valeur ne correspond pas à ce qui est attendu, une `AssertionError` est levée.

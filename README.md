# CARRON, LEOTE, WACQUIEZ

# Industrialisation des tests – Examen

Projet de test automatisé (Selenium) sur le formulaire de création de compte Wikimedia.

## Exercice 1 (Wikipedia Register page)

- **Test du formulaire de création de compte** sur `auth.wikimedia.org` (page Spécial:Créer un compte).
- Le script remplit les champs : nom d’utilisateur, mot de passe, confirmation du mot de passe, email.
- **Validation** : on vérifie que les valeurs saisies sont bien présentes dans chaque input (via `get_attribute("value")`), on sousmet le formulaire, mais un captcha empêche la création du compte.

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

### Exécuter le script

Avec le venv activé :

```bash
python ex1.py
```

ou

```bash
py ex1.py
```

## Exercice 2
Le script `ex2.py` utilise Selenium WebDriver sur [Books to Scrape](https://books.toscrape.com/) pour récupérer une liste de produits et un maximum d'informations:

- URL
- titre
- description
- catégorie
- prix
- disponibilité
- note
- image
- UPC, type de produit, prix HT/TTC, taxe, nombre d'avis

### Exécuter le script

Avec le venv activé :

```bash
python ex2.py
```

ou

```bash
py ex2.py
```

## Exercice 3 (Pytest)

Les scripts ont été transformés en tests pytest pour pouvoir être exécutés en CI.

- `**test_ex1.py**` : formulaire Wikimedia (champs remplis, sans submit).
- `**test_ex2.py**` : Books to Scrape (listing + structure d’un produit).
- `**conftest.py**` : fixture partagée du driver Chrome (headless).

```bash
pytest -v
```

Lancer un fichier ou un test précis :

```bash
pytest test_ex1.py -v
pytest test_ex2.py::test_books_toscrape_listing_charge -v
```

## CI (GitHub Actions)

Une workflow GitHub Actions exécute automatiquement les tests à chaque push et à chaque pull request sur `main` / `master`.

- Fichier : `.github/workflows/tests.yml`
- Matrice Python : `3.10`, `3.11`, `3.12`
- Étapes : checkout → setup Python (via la matrice) → `pip install -r requirements.txt` → `pytest -v`

Une fois le dépôt poussé sur GitHub, les runs sont visibles dans l’onglet **Actions**.
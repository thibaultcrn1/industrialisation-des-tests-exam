"""
Tests du scraping du site Books to Scrape.
Vérifie que la liste des livres est récupérable et que chaque produit a la structure attendue.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _scrape_product_page(driver, url):
    """Récupère les données d'une page produit."""
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.product_main h1"))
    )

    title = driver.find_element(By.CSS_SELECTOR, "div.product_main h1").text.strip()
    price = driver.find_element(By.CSS_SELECTOR, "p.price_color").text.strip()
    availability = driver.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
    description = driver.find_element(By.CSS_SELECTOR, "article.product_page > p").text.strip()
    category = driver.find_element(By.CSS_SELECTOR, "ul.breadcrumb li:nth-child(3) a").text.strip()
    rating_el = driver.find_element(By.CSS_SELECTOR, "p.star-rating")
    rating = rating_el.get_attribute("class").split()[-1]
    image_url = driver.find_element(By.CSS_SELECTOR, "div.item.active img").get_attribute("src")

    rows = driver.find_elements(By.CSS_SELECTOR, "table.table.table-striped tr")
    details = {}
    for row in rows:
        key = row.find_element(By.CSS_SELECTOR, "th").text.strip()
        value = row.find_element(By.CSS_SELECTOR, "td").text.strip()
        details[key] = value

    return {
        "url": url,
        "title": title,
        "description": description,
        "category": category,
        "price": price,
        "availability": availability,
        "rating": rating,
        "image_url": image_url,
        "upc": details.get("UPC", ""),
        "product_type": details.get("Product Type", ""),
        "price_excl_tax": details.get("Price (excl. tax)", ""),
        "price_incl_tax": details.get("Price (incl. tax)", ""),
        "tax": details.get("Tax", ""),
        "number_of_reviews": details.get("Number of reviews", ""),
    }


def test_books_toscrape_listing_charge(driver):
    """La page catalogue s'affiche et contient des cartes produit."""
    driver.get("https://books.toscrape.com/catalogue/page-1.html")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article.product_pod"))
    )
    cards = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    assert len(cards) > 0, "Aucun produit sur la page catalogue"


def test_books_toscrape_produit_structure(driver):
    """Un produit scrapé contient tous les champs attendus."""
    driver.get("https://books.toscrape.com/catalogue/page-1.html")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article.product_pod"))
    )
    first_card = driver.find_element(By.CSS_SELECTOR, "article.product_pod")
    product_url = first_card.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("href")

    product = _scrape_product_page(driver, product_url)

    expected_keys = [
        "url", "title", "description", "category", "price", "availability",
        "rating", "image_url", "upc", "product_type", "price_excl_tax",
        "price_incl_tax", "tax", "number_of_reviews",
    ]
    for key in expected_keys:
        assert key in product, f"Clé manquante dans le produit: {key}"
    assert product["title"], "Le titre ne doit pas être vide"
    assert product["price"], "Le prix ne doit pas être vide"
    assert product["url"] == product_url

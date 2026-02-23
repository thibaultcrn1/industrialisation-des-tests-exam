import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# https://books.toscrape.com/

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/catalogue/page-1.html")
time.sleep(2)

products = []

cards = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
product_urls = [card.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("href") for card in cards]

for url in product_urls:
    driver.get(url)
    time.sleep(0.4)

    title = driver.find_element(By.CSS_SELECTOR, "div.product_main h1").text.strip()
    price = driver.find_element(By.CSS_SELECTOR, "p.price_color").text.strip()
    availability = driver.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
    description = driver.find_element(By.CSS_SELECTOR, "article.product_page > p").text.strip()
    category = driver.find_element(By.CSS_SELECTOR, "ul.breadcrumb li:nth-child(3) a").text.strip()
    rating = driver.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split()[-1]
    image_url = driver.find_element(By.CSS_SELECTOR, "div.item.active img").get_attribute("src")

    rows = driver.find_elements(By.CSS_SELECTOR, "table.table.table-striped tr")
    details = {}
    for row in rows:
        key = row.find_element(By.CSS_SELECTOR, "th").text.strip()
        value = row.find_element(By.CSS_SELECTOR, "td").text.strip()
        details[key] = value

    product = {
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

    products.append(product)
    print(f"OK: {title}")

print("\n--- Résultat (JSON) ---")
print(json.dumps(products, ensure_ascii=False, indent=2))

driver.close()

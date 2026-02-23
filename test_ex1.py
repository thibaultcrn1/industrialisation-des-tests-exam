"""
Tests du formulaire de création de compte Wikimedia.
Validation des données inscrites dans les inputs, sans submit (pas de captcha).
"""

from selenium.webdriver.common.by import By


def test_wikimedia_creation_compte_champs_remplis(driver):
    """Vérifie que les champs du formulaire sont remplis et contiennent les bonnes valeurs (sans submit)."""
    url = (
        "https://auth.wikimedia.org/frwiki/wiki/Sp%C3%A9cial:Cr%C3%A9er_un_compte"
        "?useformat=desktop&usesul3=1&returnto=Wikip%C3%A9dia%3AAccueil+principal"
        "&centralauthLoginToken=ec8fed23b02068cab6e07643353e6ccd"
    )
    driver.get(url)

    USERNAME = "johndoe456782847test"
    PASSWORD = "Test1234TeSt@"
    EMAIL = "test@john.fr"

    username_input = driver.find_element(By.NAME, "wpName")
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.NAME, "wpPassword")
    password_input.send_keys(PASSWORD)

    retype_input = driver.find_element(By.NAME, "retype")
    retype_input.send_keys(PASSWORD)

    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(EMAIL)

    assert username_input.get_attribute("value") == USERNAME, (
        f"Username invalide: attendu '{USERNAME}', reçu '{username_input.get_attribute('value')}'"
    )
    assert password_input.get_attribute("value") == PASSWORD, (
        "Mot de passe invalide dans wpPassword"
    )
    assert retype_input.get_attribute("value") == PASSWORD, (
        "Mot de passe invalide dans retype"
    )
    assert email_input.get_attribute("value") == EMAIL, (
        f"Email invalide: attendu '{EMAIL}', reçu '{email_input.get_attribute('value')}'"
    )

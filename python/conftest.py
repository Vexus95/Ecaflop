import pytest

@pytest.fixture
def reset_db(page):
    """Réinitialise la base de données avant chaque test."""
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://e.se2.hr.dmerej.info/")
    page.get_by_role("link", name="Create new team").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").press("CapsLock")
    page.get_by_placeholder("Name").fill("T")
    page.get_by_placeholder("Name").press("CapsLock")
    page.get_by_placeholder("Name").fill("Test team")
    page.get_by_role("button", name="Add").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

from playwright.sync_api import sync_playwright

def test_google_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to Google
        page.goto("https://google.com")

        # Capture the title
        title = page.title()
        assert title == "Google", f"Expected title to be 'Google' but got '{title}'"

        # Take a screenshot
        page.screenshot(path="google_homepage.png")

        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_google_navigation()
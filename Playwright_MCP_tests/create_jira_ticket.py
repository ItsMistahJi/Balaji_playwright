from playwright.sync_api import sync_playwright

def create_jira_ticket():
    with sync_playwright() as p:
        # Launch Edge browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the JIRA URL
        page.goto("https://JIRA/CreateIssue.jspa")

        # Scrape the page to get all elements (optional, for debugging purposes)
        # print(page.content())

        # Find the "Labels" text box and fill it with "SKY"
        page.fill("label:has-text('Labels') + input", "test")

        # Tick the checkbox before "Sprint" next to "Branch"
        page.check("label:has-text('Sprint') + input")

        # Take a screenshot
        page.screenshot(path="page_screenshot.png")

        # Close the browser
        #browser.close()

if __name__ == "__main__":
    create_jira_ticket()
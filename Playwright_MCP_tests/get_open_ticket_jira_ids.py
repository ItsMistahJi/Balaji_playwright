from playwright.sync_api import sync_playwright

def get_open_ticket_jira_ids():
    # Start Playwright
    with sync_playwright() as p:
        # Launch Edge browser
        browser = p.chromium.launch(channel="msedge", headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the specified URL
        url = "https://JIRA/secure/Dashboard.jspa"
        page.goto(url)

        # Take a screenshot of the page
        screenshot_path = "page_screenshot.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")

        # Find ticket JIRA IDs with the specified span class and value
        open_tickets = []
        elements = page.query_selector_all("span.jira-issue-status-tooltip-title")
        for element in elements:
            if element.inner_text() == "Open":
                anchor = element.evaluate_handle("el => el.closest('a')")
                if anchor:
                    ticket_id = anchor.get_attribute("data-issue-key")
                    if ticket_id:
                        open_tickets.append(ticket_id)

        # Save the ticket IDs to a text file
        output_file = "open_ticket_ids.txt"
        with open(output_file, "w") as file:
            for ticket_id in open_tickets:
                file.write(ticket_id + "\n")

        print(f"Open ticket JIRA IDs saved to {output_file}")

        # Close the browser
        browser.close()

if __name__ == "__main__":
    get_open_ticket_jira_ids()
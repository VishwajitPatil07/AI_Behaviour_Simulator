from playwright.sync_api import sync_playwright
import behavior  # Imports our human behavioral brain

def run_human_web_agent():
    print("[Agent] Starting Web Browser Automation...")
    with sync_playwright() as p:
        # Launch browser in headed mode so we can watch it work
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 1. Navigate to a target site
        print("[Agent] Navigating to example.com...")
        page.goto("https://example.com")
        
        # 2. Add a dynamic human reading pause
        behavior.human_delay(target_seconds=3.0, deviation=0.7)
        
        # 3. Take a humanized action (Simulate clicking a link with offset)
        print("[Agent] Locating elements...")
        link = page.locator("a")
        if link.count() > 0:
            # Instead of a rigid instant click, add a micro cognitive delay
            behavior.human_delay(target_seconds=1.0, deviation=0.2)
            print("[Agent] Clicking link with humanized pacing...")
            link.first.click()
            
        # 4. Another delay to simulate looking at the new page
        behavior.human_delay(target_seconds=2.5)
        
        # Save our proof of work
        page.screenshot(path="human_screenshot.png")
        print("[Agent] Screenshot saved successfully.")
        
        browser.close()
        print("[Agent] Web Agent run completed cleanly.")

if __name__ == "__main__":
    run_human_web_agent()

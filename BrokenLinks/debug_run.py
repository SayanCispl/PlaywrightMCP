from playwright.sync_api import sync_playwright
from urllib.parse import urlparse, urljoin

BASE_URL = "https://frymaster.bwd-003.borders.dev/service#Software"
PASSWORD = "tech"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    request_ctx = p.request.new_context()
    try:
        print('Going to', BASE_URL)
        page.goto(BASE_URL, wait_until='networkidle', timeout=30000)
        print('Page loaded:', page.url)
        # try to find password
        selectors = ['input[type="password"]','input[name="password"]','input#password','input[placeholder*="password"]']
        pwd = None
        for sel in selectors:
            loc = page.locator(sel)
            cnt = loc.count()
            print(f"Selector {sel} count={cnt}")
            if cnt>0:
                pwd = loc.nth(0)
                break
        if not pwd:
            print('Password field not found')
        else:
            pwd.fill(PASSWORD)
            print('Filled password')
        # find view button
        btn_selectors = ['button:has-text("View")','button:has-text("VIEW")','button:has-text("Show")','input[type="submit"]','button[type="submit"]']
        btn=None
        for sel in btn_selectors:
            loc=page.locator(sel)
            cnt=loc.count()
            print(f"Button selector {sel} count={cnt}")
            if cnt>0:
                btn=loc.nth(0)
                break
        if not btn:
            print('View button not found')
        else:
            btn.click()
            print('Clicked view button')
        # check software content
        software_locators = ['#Software','text=Software','h1:has-text("Software")','h2:has-text("Software")','section:has-text("Software")']
        found=False
        for sel in software_locators:
            loc=page.locator(sel)
            cnt=loc.count()
            print(f"Software selector {sel} count={cnt}")
            if cnt>0 and loc.nth(0).is_visible():
                text=loc.nth(0).inner_text().strip()
                print('Found text length',len(text))
                found=True
                break
        print('Software found?',found)
        # collect links
        anchors=page.locator('a[href]')
        print('Anchors count', anchors.count())
        links=set()
        for i in range(anchors.count()):
            href=anchors.nth(i).get_attribute('href')
            if not href:
                continue
            full=urljoin(page.url, href)
            links.add(full)
        print('Collected links:', len(links))
        for l in sorted(links):
            print('-', l)
    finally:
        request_ctx.dispose()
        browser.close()


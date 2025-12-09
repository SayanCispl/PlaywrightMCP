from playwright.sync_api import sync_playwright, TimeoutError
import pytest
import time
from urllib.parse import urljoin, urlparse

BASE_URL = "https://frymaster.bwd-003.borders.dev/service#Software"
PASSWORD = "tech"
REQUEST_TIMEOUT = 10
RETRY_COUNT = 2
ALLOWLIST = [
    # Add substrings or exact URLs to ignore 404s
]


def normalize_url(base, link):
    if not link:
        return None
    link = link.strip()
    if link.startswith(("javascript:", "mailto:", "tel:", "data:")):
        return None
    if link.startswith("#"):
        return None
    return urljoin(base, link)


def is_allowlisted(u: str) -> bool:
    if not u:
        return False
    for sub in ALLOWLIST:
        if sub in u:
            return True
    return False


def http_status(request_ctx, url):
    last_exc = None
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            # try HEAD first
            try:
                resp = request_ctx.head(url, timeout=REQUEST_TIMEOUT * 1000)
                status = resp.status
                # Some servers respond to HEAD with 405; treat by falling back
                if status == 405 or status >= 400:
                    resp = request_ctx.get(url, timeout=REQUEST_TIMEOUT * 1000)
                    status = resp.status
            except Exception:
                # fallback to GET if HEAD failed
                resp = request_ctx.get(url, timeout=REQUEST_TIMEOUT * 1000)
                status = resp.status
            return status
        except Exception as e:
            last_exc = e
            time.sleep(0.5 * attempt)
    raise last_exc


@pytest.mark.broken_links
def test_service_software_view_and_broken_links():
    visited = set()
    found_links = set()
    broken_links = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        request_ctx = p.request.new_context()

        try:
            page.goto(BASE_URL, wait_until='networkidle', timeout=30000)

            # find password field - try a set of selectors
            pwd_selectors = [
                'input[type="password"]',
                'input[name="password"]',
                'input#password',
                'input[placeholder*="password"]',
            ]
            pwd = None
            for sel in pwd_selectors:
                try:
                    locator = page.locator(sel)
                    if locator.count() > 0:
                        pwd = locator.nth(0)
                        break
                except Exception:
                    continue

            assert pwd is not None, f"Password field not found with selectors: {pwd_selectors}"
            pwd.fill(PASSWORD)

            # find and click view button
            btn_selectors = [
                'button:has-text("View")',
                'button:has-text("VIEW")',
                'button:has-text("Show")',
                'input[type="submit"]',
                'button[type="submit"]',
            ]
            btn = None
            for sel in btn_selectors:
                try:
                    locator = page.locator(sel)
                    if locator.count() > 0:
                        btn = locator.nth(0)
                        break
                except Exception:
                    continue

            assert btn is not None, f"View button not found with selectors: {btn_selectors}"
            btn.click()

            # wait for software content
            software_locators = [
                '#Software',
                'text=Software',
                'h1:has-text("Software")',
                'h2:has-text("Software")',
                'section:has-text("Software")',
            ]
            software_found = False
            for sel in software_locators:
                try:
                    locator = page.locator(sel)
                    if locator.count() > 0 and locator.nth(0).is_visible():
                        text = locator.nth(0).inner_text().strip()
                        if len(text) > 5:
                            software_found = True
                            break
                except TimeoutError:
                    continue
                except Exception:
                    continue

            assert software_found, "Software content not visible after viewing"

            # collect links
            anchors = page.locator('a[href]')
            for i in range(anchors.count()):
                try:
                    href = anchors.nth(i).get_attribute('href')
                    full = normalize_url(page.url, href)
                    if not full:
                        continue
                    if full in found_links:
                        continue
                    found_links.add(full)
                except Exception:
                    continue

            # check same-origin and HTTP status
            parsed_base = urlparse(BASE_URL)
            for link in sorted(found_links):
                purl = urlparse(link)
                if purl.scheme not in ("http", "https"):
                    continue
                if purl.scheme != parsed_base.scheme or purl.netloc != parsed_base.netloc:
                    # skip external
                    continue
                if is_allowlisted(link):
                    print(f"Skipping allowlisted: {link}")
                    continue
                print(f"Checking: {link}")
                try:
                    status = http_status(request_ctx, link)
                    if status == 404:
                        broken_links.append((link, status))
                except Exception as e:
                    broken_links.append((link, str(e)))

        finally:
            request_ctx.dispose()
            browser.close()

    if broken_links:
        print("Broken links found:")
        for u, s in broken_links:
            print(f" - {u} -> {s}")

    assert not broken_links, f"Found {len(broken_links)} broken links"

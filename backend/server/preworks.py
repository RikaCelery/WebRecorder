from urllib.parse import urlparse
from playwright.async_api import Page as page
async def do(p:page):
    host = urlparse(p.url).hostname
    if host.endswith("pornhub.com"):
        element = page.wait_for_selector(".gtm-event-age-verification",timeout=2000)
        if element is not None:
            await element.click()
    ...
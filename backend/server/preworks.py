from urllib.parse import urlparse
from playwright.async_api import Page
async def do(p:Page):
    host = urlparse(p.url).hostname
    if host.endswith("pornhub.com"):
        element = await p.wait_for_selector(".gtm-event-age-verification",timeout=8000)
        if element is not None and element.is_visible():
            await element.click()
    ...
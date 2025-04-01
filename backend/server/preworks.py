import asyncio
from urllib.parse import urlparse
from playwright.async_api import Page
async def do(page:Page):
    host = urlparse(page.url).hostname
    if host.endswith("pornhub.com"):
        await page.goto("https://www.pornhub.com")
        await page.get_by_role("button", name="I am 18 or older - Enter").click()
        await asyncio.sleep(2)
    ...
from playwright.async_api import Page

from app.jobs import BaseJob


class ScreenshotJob(BaseJob):
    NAME = "screenshot"

    url: str | None = None
    html: str | None = None
    full_page: bool = False

    async def execute(self, page: Page) -> bytes:
        if self.url:
            await page.goto(self.url)
        elif self.html:
            await page.set_content(self.html)

        return await page.screenshot(full_page=self.full_page)

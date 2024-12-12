from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

def Ghtml(WUrl, SBrowser=True, SStName = ''):
    with sync_playwright() as p:
        Browser = p.chromium.launch(headless=not SBrowser)
        page = Browser.new_page()
        page.goto(url=WUrl)

        page.wait_for_load_state('networkidle')
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_timeout(1000)

        if SStName != '':
            page.screenshot(full_page=True, path=f'./{SStName}.png')

        pageHtml = page.inner_html('body')

        PData = HTMLParser(pageHtml)

        return PData
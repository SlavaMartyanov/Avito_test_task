import asyncio
from playwright.async_api import async_playwright

async def take_counter_screenshots(url, counter_data):
    async with async_playwright() as p:
        browser = await p.firefox.launch()  # Launch Firefox browser
        page = await browser.new_page()
        await page.goto(url)

        for i, counter in enumerate(counter_data):
            selector = counter["selector"]
            name = f"test_case_{i+1}"  # Name screenshots according to test case number

            try:
                # Wait for counter element to be visible
                await page.wait_for_selector(selector, state="visible")
                counter_element = await page.query_selector(selector)

                # Take screenshot of the counter element
                await counter_element.screenshot(path=f"output/{name}.png")
                print(f"Screenshot for test case {i+1} saved as output/{name}.png")
            except Exception as e:
                print(f"Error taking screenshot for test case {i+1}: {e}")

        await browser.close()

# Counter data with provided selectors
counter_data = [
    {"selector": "div.desktop-impact-item-eeQO3:nth-child(2) > div:nth-child(2) > div:nth-child(1)"},
    {"selector": "div.desktop-disabled-kdOve:nth-child(3) > div:nth-child(1)"},
    {"selector": "div.desktop-impact-item-eeQO3:nth-child(6) > div:nth-child(2) > div:nth-child(1)"}
]

url = "https://www.avito.ru/avito-care/eco-impact"  # URL of the website

asyncio.run(take_counter_screenshots(url, counter_data))
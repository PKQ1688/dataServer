import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

app = FirecrawlApp(api_key=firecrawl_api_key)

# Scrape a single URL
url = "https://www.usatoday.com/money/blueprint/investing/cryptocurrency/bitcoin-price-today-08-07-2024/"
scraped_data = app.scrape_url(url)

print(scraped_data)

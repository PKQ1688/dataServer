import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

app = FirecrawlApp(api_key=firecrawl_api_key)

# Scrape a single URL
url = 'https://movie.douban.com/top250'
scraped_data = app.scrape_url(url)

print(scraped_data)

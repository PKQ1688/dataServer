import asyncio

from crawlee.beautifulsoup_crawler import (
    BeautifulSoupCrawler,
    BeautifulSoupCrawlingContext,
)


async def main() -> None:
    crawler = BeautifulSoupCrawler(
        # Limit the crawl to max requests. Remove or increase it for crawling all links.
        max_requests_per_crawl=10,
    )

    # Define the default request handler, which will be called for every request.
    @crawler.router.default_handler
    async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
        context.log.info(f"Processing {context.request.url} ...")

        # Extract data from the page.
        data = {
            "url": context.request.url,
            "title": context.soup.title.string if context.soup.title else None,
        }

        print(data)

        # Push the extracted data to the default dataset.
        # await context.push_data(data)

        # Enqueue all links found on the page.
        # await context.enqueue_links()

    # Run the crawler with the initial list of URLs.
    await crawler.run(["https://movie.douban.com/top250"])


if __name__ == "__main__":
    asyncio.run(main())

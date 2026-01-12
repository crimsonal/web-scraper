from pathlib import Path 

import scrapy 

class QuotesSpider(scrapy.Spider):
    name = "article"

    async def start(self):
        url="https://archive.is/fn6iL"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f"article-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file{filename}")
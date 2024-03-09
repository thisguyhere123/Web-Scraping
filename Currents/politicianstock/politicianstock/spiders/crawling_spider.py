from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    #type url in perentheses below
    allowed_domains = ["quiverquant.com"]
    #type where you want it to start on site below
    start_urls = ["https://www.quiverquant.com/congresstrading/"]

    rules = (
        Rule(LinkExtractor(allow="congresstrading/trade"), callback ="parse_item"),
        Rule(LinkExtractor())
        #here you show what area of site spider is allowed to crawl
    )

    def parse_item(self, response):
        yield {
            "stockname": response.css(".product_main span.positive::text").get(),
        }sw
import scrapy
from myproject.items import SnpPerformanceItem


class SnpPerformanceSpider(scrapy.Spider):
    name = "snp_performance"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        # Extracting table rows
        rows = response.xpath('//div[@class="table-responsive"]/table/tbody/tr')

        for row in rows:
            # Extracting data from each row
            number = row.xpath('./td[1]/text()').get()
            company = row.xpath('./td[2]/a/text()').get()
            symbol = row.xpath('./td[3]/a/text()').get()
            ytd_return = row.xpath('./td[4]/text()').get()

            # Creating an instance of the item class and yielding it
            item = SnpPerformanceItem()
            item['Number'] = number
            item['Company'] = company
            item['Symbol'] = symbol
            item['YTD_Return'] = ytd_return
            yield item



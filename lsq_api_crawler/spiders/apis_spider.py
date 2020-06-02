import scrapy


class APIsSpider(scrapy.Spider):
    name = 'apis'
    start_urls = [
        'https://apidocs.leadsquared.com'
    ]

    def parse(self, response):
        for li in response.css('.bellows-menu-item.bellows-menu-item-type-post_type.bellows-menu-item-object-page.bellows-menu-item-has-children'):
            yield {
                'title': li.xpath('.//a/span/text()').get(),
                'subMenu': list(map(lambda ul: {
                    'title': ul.xpath('a/span/text()').get(),
                    'subMenu': list(map(lambda li: {
                        'title': li.xpath('span/text()').get(),
                        'href': li.xpath('@href').get()
                    }, ul.xpath('ul/li/a'))),
                }, li.xpath('ul/li')))
            }

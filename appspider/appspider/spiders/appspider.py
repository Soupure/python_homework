from urllib import parse

import scrapy


class AppSpider4399(scrapy.Spider):
    name = '4399'
    baseurl = 'http://www.4399.cn/search.html?w='

    def __init__(self, kw='', **kwargs):
        self.start_urls = [self.baseurl + parse.quote(kw)]
        super().__init__(**kwargs)

    def parse(self, response):
        root = "//div[@class='f-tabcon']/ul/li"
        for app in response.xpath(root):
            yield {
                'title': app.xpath("./h4/a/text()").get(),
                'url': app.xpath("./h4/a/@href").get(),
                'icon': app.xpath("./a/img/@src").get(),
                'desc': app.xpath("./div[@class='m-info']/p[2]/text()").get(),
            }


class AppSpider360(scrapy.Spider):
    name = '360'
    baseurl = 'http://zhushou.360.cn/search/index/?kw='

    def __init__(self, kw, **kwargs):
        self.start_urls = [self.baseurl + parse.quote(kw)]
        super().__init__(**kwargs)

    def parse(self, response):
        root = "//div[@class='main']/div/ul/li/dl/dd/h3/a[string-length(@title)>0]/../../../.."
        for app in response.xpath(root):
            yield {
                'title': app.xpath("./dl/dd/h3/a/@title").get(),
                'url': app.xpath("./dl/dt/a/@href").get(),
                'icon': app.xpath("./dl/dt/a/img/@src").get(),
                'desc': app.xpath("./dl/dd/p/text()").get(),
            }


class AppSpiderAnzhi(scrapy.Spider):
    name = 'anzhi'
    baseurl = 'http://www.anzhi.com/search.php?keyword='

    def __init__(self, kw='', **kwargs):
        self.start_urls = [self.baseurl + parse.quote(kw)]
        super().__init__(**kwargs)

    def parse(self, response):
        root = "//div[contains(@class,'app_list')]/ul/li"
        for app in response.xpath(root):
            yield {
                'title': app.xpath("./div[@class='app_info']/span/a/text()").get(),
                'url': app.xpath("./div[@class='app_icon']/a/@href").get(),
                'icon': app.xpath("./div[@class='app_icon']/a/img/@src").get(),
                'desc': app.xpath("./div[@class='app_info']/p/text()").get(),
            }

import scrapy
from ufrpe.items import UfrpeItem


class PlebotSpider(scrapy.Spider):
    name = 'plebot'
    allowed_domains = ['ufrpe.br']
    start_urls = ['http://www.ufrpe.br/br/content/faq-do-per%C3%ADodo-letivo-excepcional']

    def parse(self, response, **kwargs):
        for link in response.xpath('/html//article/div/div/div/p/a/@href').extract():
            yield response.follow(link, callback=self.parse_article)

    def parse_article(self, response):
        link = response.url
        resposta = response.xpath('//article/div/div/div/p/text()').extract()[0]
        pergunta = response.xpath('//section/h1/text()').extract()[0]
        notice = UfrpeItem(pergunta=pergunta, resposta=resposta, link=link)
        yield notice

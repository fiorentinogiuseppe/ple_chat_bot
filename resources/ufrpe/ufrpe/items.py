# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UfrpeItem(scrapy.Item):
    pergunta = scrapy.Field()
    resposta = scrapy.Field()
    link = scrapy.Field()
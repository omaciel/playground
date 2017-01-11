# -*- coding: utf-8 -*-
import scrapy


class EpisodesSpider(scrapy.Spider):
    name = "episodes"
    allowed_domains = [
            'itunes.apple.com/br/podcast/castalio-podcast/id446259197'
            ]
    start_urls = [
            'http://itunes.apple.com/br/podcast/castalio-podcast/id446259197/'
                ]

    def parse(self, response):
        episodes = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div/table/tbody/tr/td[2]/'
            'span/span[2]/text()').extract()

        cont = 0
        castalio = {}
        for episode in episodes:
            castalio[episode] = response.xpath(
                '//*[@id="content"]/div/div[2]/div[2]/div/table/tbody/tr/'
                'td[4]/span/span/text()')[cont].extract()
            cont += 1
        return castalio

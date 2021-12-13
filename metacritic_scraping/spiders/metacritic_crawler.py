import scrapy
from scrapy.linkextractors import LinkExtractor
import numpy as np

class MetacriticCrawlerSpider(scrapy.Spider):
    name = 'metacritic_crawler'
    allowed_domains = ["www.metacritic.com"]
    start_urls = ["https://www.metacritic.com/browse/games/release-date/new-releases/ps5/userscore"]
    def parse(self, response):
        platform_texts = [platform.strip() for platform in response.css(".mcmenu.platform ul li a::text").getall() if platform.strip() != '']
        platform_uri = ["-".join(platform_text.lower().split()) for platform_text in platform_texts]
        platform_links = self.__platform_links(platform_uri)
        for platform in platform_links:
            yield scrapy.Request(
                url=platform,
                callback=self.parse_platforms,
            )

    def __platform_links(self, platforms_uri):
        return [f"https://www.metacritic.com/browse/games/release-date/new-releases/{platform_uri}/userscore" 
                                                                        for platform_uri in platforms_uri]    
        
    def parse_platforms(self, response):
        links = LinkExtractor(allow_domains=self.allowed_domains,
                                restrict_css="div div.browse_list_wrapper tr td.clamp-summary-wrap a.title")
        for link in links.extract_links(response):
            yield scrapy.Request(
                url=link.url,
                callback=self.parse_metacritic
            )

    def __extract_text(self, response, csspath, aslist=False):
        if not aslist:
            return response.css(csspath).get().strip()
        else:
            return ", ".join(response.css(csspath).getall()).strip()

    def __score_treatment(self, response, csspath):
        score = response.css(csspath).get()
        if score is None or score == "tbd":
            return np.nan
        return float(score) if "." in score else int(score)
        

    def parse_metacritic(self, response):
        # review type: no score yet, Generally unfavorable, mixed or average, generally favorable, etc
        yield {
            "title": self.__extract_text(response, "a h1::text"), 
            "genre": self.__extract_text(response, ".product_genre .data::text", aslist=True),
            "platform": self.__extract_text(response, "span.platform a::text"),
            "developer":self.__extract_text(response, "span.data a.button::text"),
            "publisher": self.__extract_text(response, ".publisher span.data a::text"),
            "fn_userscore_type": self.__extract_text(response, ".feature_userscore .desc::text"),
            "fn_userscore": self.__score_treatment(response, ".metascore_w.user::text"),
            "fn_metascore_type": self.__extract_text(response, ".summary .desc::text"),
            "fn_metascore": self.__score_treatment(response, ".metascore_w span::text"),
        }

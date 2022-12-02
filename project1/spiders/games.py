import scrapy


class GamesSpider(scrapy.Spider):
    name = 'games'
    start_urls = ['http://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json']

    def parse(self, response):
        games = response.json()

        yield games

# Metacritic Crawler an Scraping
Metacritic Crawler and Scraping using Scrapy Framework in order to create a new dataset and analyze it.

The Metacritic spider crawler analyze news (Dec. 2021) games by userscores filtered website. The Metacritic spider crawler it aims to be versatile and
scaleable.

For generate dataset with this spider crawler uses:
`scrapy crawl metacritic_crawler -o random_name.csv` or `scrapy crawl metacritic_crawler -o random_name.json`

PS: is needed to install all dependencies to work (Numpy and Scrapy) in your machine, scrapyvenv virtual environment of this repository, or your own virtualenv
PSS: np.nan has problem with JSON files

if you want save in other dir, you can do this:
`scrapy crawl metacritic_crawler -o datasets/metacritic-newest-games.json`

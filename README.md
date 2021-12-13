# Metacritic - Crawler and Scraping
Metacritic Crawler and Scraping using Scrapy Framework in order to create a new dataset and analyze it.

The Metacritic spider crawler analyze games by userscores filtered website. The Metacritic spider crawler it aims to be versatile and
scaleable. 

For generate dataset with this spider crawler uses:<br>
`scrapy crawl metacritic_crawler -o random_name.csv` or `scrapy crawl metacritic_crawler -o random_name.json`

if you want save in other dir, you can do:
`scrapy crawl metacritic_crawler -o datasets/metacritic-newest-games.json`

PS: is needed to install all dependencies to work (Numpy and Scrapy) in your machine or your own virtualenv <br>

PSS: `np.nan` has problem with JSON files

The dataset variables: <br>
`title`: Title of the game <br>
`genre`: Genre or genres of the game <br>
`platform`: Platform of the game, can has be repeated. <br>
`developer`: Developer's company of the game. <br>
`publisher`: Publisher's company of the game. <br>
`fn_usercore_type`: Final/Average User's score of the game type(how accepted the game was by the users who rated it) <br>
`fn_userscore`: Final/Average User's score of the game. <br>
`fn_metascore_type`: Final/Average Metacritic's score of the game type(how accepted the game was by the critics who rated it) <br>
`fn_metascore`: Final/Average Metacritic's score of the game <br>


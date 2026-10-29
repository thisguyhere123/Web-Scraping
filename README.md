# Web-Scraping

My first scraping project, from 2024: a [Scrapy](https://scrapy.org) crawler that follows the congressional
stock-trade pages on quiverquant.com and yields one item per trade page. It obeys robots.txt
(`ROBOTSTXT_OBEY = True`) and stays on the one allowed domain.

```
pip install scrapy
cd Currents/politicianstock
scrapy crawl mycrawler -O trades.json
```

The CSS selector in `parse_item` was written against the site as it was in 2024 and may need updating.

`scripts/keyboard_macro.py` is an unrelated keyboard record-and-replay experiment. It used to sit in the spiders
folder, where Scrapy would import (and run) it on every crawl.

This later grew into **Scrape Anything**, a full scraping service. See the
[portfolio](https://thisguyhere123.github.io/portfolio/).

import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from crawl import Crawler

if __name__ == "__main__":
    crawler = Crawler(api_key='9R5ijwSplYX8NmTMqLtHNoqBBzHLArhHpWXxCuXBS1') # Put your API key in .env file
    crawler.download_historical_data(category="label", symbol="DYDX", location='./data')
    print("Lastest data: ", crawler.get_lastest_data(category="crypto", symbol="BTCUSDT"))
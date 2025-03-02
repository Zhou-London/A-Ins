import requests
from bs4 import BeautifulSoup
import time
import random


class BingNewsCrawler:
    def __init__(self, topic, num_urls):
        self.topic = topic
        self.num_urls = num_urls
        self.base_url = "https://www.bing.com/news/search"
        self.search_url = f"{self.base_url}?q={self.topic}&form=QBNH"

    def get_news_urls(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(self.search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", class_="title")

        news_urls = []
        for link in links:
            href = link.get("href")
            if href and not href.startswith("/"):
                news_urls.append(href)
                if len(news_urls) >= self.num_urls:
                    break

        return news_urls

from Services.openai_service import openai_agent
from Services.openai_service import solr_agent
from Services.bing_crawler import BingNewsCrawler


# crawler = BingNewsCrawler("technology", 10)
# urls = crawler.get_news_urls()
# for url in urls:
#     print(url)


# print(openai_agent.process_image({"content": "flower"}))
# response = openai_agent.process_news("politics")

response = openai_agent.process_news("art")

# print(solr_agent.search_posts_test("art"))

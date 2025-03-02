"""
Service of Solr
"""

from Config.solr_config import solr


class Agent:

    def __init__(self):
        results = solr.search("*:*", rows=0)
        self.count = results.hits + 1

    def insert_json(self, json_file):
        self.insert_post(
            json_file["title"],
            json_file["content"],
            json_file["image"],
            json_file["tags"],
        )

    def insert_post(self, title, content, image, tags):

        post_id = f"id{self.count}"
        post = {
            "id": post_id,
            "title": title,
            "content": content,
            "image": image,
            "tags": tags,
        }
        self.count += 1

        solr.add([post])
        solr.commit()
        return post_id

    def delete_post(self, ids):
        solr.delete(id=ids)
        solr.commit()

    def search_posts(self, tag):
        query = f"tags:{tag}"
        results = solr.search(query)
        return [dict(result) for result in results]

    def search_posts_test(self, tag):
        query = f"tags:{tag}"
        results = solr.search(query, fl="id,title")
        return [dict(result) for result in results]

    def info(self):
        query = "*:*"
        results = solr.search(query, fl="id, title")
        return [dict(result) for result in results]


solr_agent = Agent()

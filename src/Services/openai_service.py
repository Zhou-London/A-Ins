"""
Service of OpenAI
"""

from Config.openai_config import openai_client
from Models.response_models import OpenAI_Post
from Services.bing_crawler import BingNewsCrawler
from Services.base64_encoder import ImageEncoder
from Services.solr_service import solr_agent
import json


class Agent:
    def __init__(self):
        self.client = openai_client

    def check_status(self):
        # Get response
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    # Pre-prompt
                    "role": "developer",
                    "content": "You are a helpful assistant.",
                },
                {
                    # Prompt
                    "role": "user",
                    "content": "Hello!",
                },
            ],
            max_tokens=10,
        )

        return response.choices[0].message.content

    def process_news(self, tag):

        print("Calling crawlers...")

        crawler = BingNewsCrawler(tag, 5)
        urls = crawler.get_news_urls()
        if len(urls) > 0:
            url = urls[2]
            print("Crawler is working.(1/4)")
        else:
            url = "None"
            print("Crawler is not working")
            return False

        # Get response
        print("Calling Chat-GPT")

        response = self.client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {
                    "role": "developer",
                    "content": """
                    You will be given a URL.
                    Read through the website and conclude the information into
                    title, content, tags and an image.
                    The image doens't need anything, simply leave it empty.
                    The url of image will be added later elsewhere.
                    There are only these tags:
                    -   Technology
                    -   Amusement
                    -   Art
                    Reply in English.
                    Do not have any more tag that have not mentioned above.
                    The title should be concise and interesting.
                    Your tone should be humorous and funny.
                    Like you are talking with your friends.
                    Store these information in JSON format.
                    Keep your answer short and concise.
                    """,
                },
                {
                    "role": "user",
                    "content": url,
                },
            ],
            response_format=OpenAI_Post,
        )

        if response is not None:
            print("OpenAI is working.(2/4)")
        else:
            print("OpenAI is not working")
            return False

        json_file = self.process_image(
            response.choices[0].message.parsed.model_dump_json()
        )

        # Insert json to the DataBase
        print("Adding data to DB...")

        solr_agent.insert_json(json_file)

        print("Success.(4/4)")

        return True

    # Pass in json file
    def process_image(self, json_str):

        # Draw the image
        parsed_json = json.loads(json_str)

        print("Calling Dalle-2")

        response = self.client.images.generate(
            model="dall-e-2",
            prompt=parsed_json["content"],
            size="256x256",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        encoder = ImageEncoder(image_url)
        parsed_json["image"] = encoder.get_base64()

        print("Dalle-2 is working.(3/4)")

        # Return the new json file
        return parsed_json


openai_agent = Agent()

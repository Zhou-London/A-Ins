import requests
import base64


class ImageEncoder:
    def __init__(self, image_url):
        """Init URL"""
        self.image_url = image_url

    def get_base64(self):
        """Convert to Base64"""
        try:
            # 下载图片
            response = requests.get(self.image_url, timeout=10)
            if response.status_code != 200:
                raise Exception(f"Failed to download the image: {response.status_code}")

            # 将图片数据编码为 Base64
            image_data = response.content
            base64_encoded = base64.b64encode(image_data).decode("utf-8")
            return base64_encoded

        except Exception as e:
            print(f"Error: {e}")
            return None

        """
        try:
            filename = "/Users/zhou/repo/ains/src/Services/base.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(base64_encoded)
            print(f"Base64 saved to {filename}")
        except Exception as e:
            print(f"Failed to save the file: {e}")
        """


if __name__ == "__main__":
    url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-wWx07DQDgNVbOeA0LAai1xmi/user-mGNRaztBR1BNXJMtPHcIimc2/img-h5Z0jjRF2m7f5wC8zmNzdRHq.png?st=2025-03-01T16%3A26%3A12Z&se=2025-03-01T18%3A26%3A12Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-03-01T01%3A46%3A59Z&ske=2025-03-02T01%3A46%3A59Z&sks=b&skv=2024-08-04&sig=YAEnnnCKDMCYeE69V14HCjJ/o/X4aDkISRqKtyenXHI%3D"
    encoder = ImageEncoder(url)
    base64_str = encoder.get_base64()
    if base64_str:
        print("Base64 :", base64_str[:10], "...")

import requests

"""
schema_url = "http://localhost:8983/solr/posts/schema"
schema_payload = {
    "add-field": [
        {"name": "id", "type": "string", "stored": True, "indexed": True},
        {"name": "title", "type": "string", "stored": True, "indexed": True},
        {"name": "content", "type": "text_general", "stored": True, "indexed": True},
        {"name": "image", "type": "string", "stored": True, "indexed": False},
        {
            "name": "tags",
            "type": "string",
            "multiValued": True,
            "stored": True,
            "indexed": True,
        },
    ]
}
"""

# response = requests.post(schema_url, json=schema_payload)
response = requests.get("http://localhost:8983/solr/posts/schema")
print(response.json())

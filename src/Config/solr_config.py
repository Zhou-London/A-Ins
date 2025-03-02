"""
Configuration of Solr
"""

import pysolr
import requests

# Configure solr connection
solr_url = "http://localhost:8983/solr/posts"
solr = pysolr.Solr(solr_url, timeout=10)

try:
    solr.ping()
except Exception as e:
    print("Failed to connect to Sole")

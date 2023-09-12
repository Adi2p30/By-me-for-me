import requests
import sys
import os
import ssl
import google
from googlesearch import search
ssl._create_default_https_context = ssl._create_stdlib_context
def download_pdf(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)
topics = ["ADD_TOPICS_HERE"]

#hf
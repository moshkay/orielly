import requests
import django
import os
from django.conf import settings
# from oreilly_api import oreilly_api_defaults

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oreilly.settings")
django.setup()
import json
from oreilly_api.models import Book
# language= python


resp = requests.get('https://learning.oreilly.com/api/v2/search/?query=python&limit=200')
if resp.status_code == 200:
    output = resp.json()
    results = output['results']

    for item in results:
        # print(item)
        # exit()
        title = item.get('title')
        isbn = item.get('isbn')
        authors = item.get('authors')
        desc = item.get("description")
        Book.objects.create(title=title, isbn=isbn, author=json.dumps(authors), description=desc)

else:
    print(resp.status_code)
    print(f"the query's response code is {resp.status_code}")

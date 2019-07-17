from django.test import TestCase

# Create your tests here.
import requests

BASE_URL = 'http://127.0.0.1:8085/'
ENDPOINT = 'json_data/'
r=requests.get(BASE_URL+ENDPOINT)
data = r.json()
print(data)

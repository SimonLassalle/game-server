#http://192.168.99.100:8888/
import requests

r = requests.get("http://192.168.99.100:8889")
print(r.text)

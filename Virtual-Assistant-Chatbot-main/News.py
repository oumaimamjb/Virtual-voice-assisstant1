# news.py
import requests
articles = []
class News:
    def __init__(self):
        self.key = "8b23e03ba0e3453384c78b77d2ad341b"

    def get_top_headlines(self):
        api_address = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + self.key
        json_data = requests.get(api_address).json()

        
        for i in range(3):
            articles.append("Number " + str(i+1) + ": " + json_data['articles'][i]['title'])
        return articles




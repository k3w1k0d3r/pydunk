import requests
class API():
    def __init__(self, urls=None):
        self.urls = urls
        if(self.urls is None):
            self.urls = {
                "location": "https://www.dunkindonuts.com/bin/servlet/dsl",
                "menu": "https://www.dunkindonuts.com/bin/servlet/getMenuItems",
            }
    def post(self, url_name, data={}):
        s = requests.post(self.urls[url_name], data=data)
        return s.json()
    def get(self, url_name, data={}):
        s = requests.get(self.urls[url_name], data=data)
        return s.json()

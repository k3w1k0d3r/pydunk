from .api import API
import requests
class Category():
    def __init__(self, name, page_title, alt_text, page_path):
        self.name = name
        self.page_title = page_title
        self.alt_text = alt_text
        self.page_path = page_path
        self.items = []
    def add_item(self, name, page_title, alt_text, page_path):
        self.items.append(Item(name, page_title, alt_text, page_path, self))
class Item():
    def __init__(self, name, page_title, alt_text, page_path, category):
        self.name = name
        self.page_title = page_title
        self.alt_text = alt_text
        self.page_path = page_path
        self.category = category
class Menu():
    def __init__(self, api: API=None):
        self.api = api
        if(self.api is None):
            self.api = API()
        self.menu = []
        self.get_menu()
    def get_menu(self):
        res = self.api.get("menu")
        category_list = res["list"]
        for i in category_list:
            self.menu.append(Category(i["ctatitle"], i["pagetitle"], i["alttext"], i["pagepath"]))
            for j in i["sublist"]:
                self.menu[-1].add_item(j["ctatitle"], j["pagetitle"], j["alttext"], j["pagepath"])

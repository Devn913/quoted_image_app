from os import error
import requests
import datetime


class ImageGrab:

    def __init__(self, list = ["random"]):
        self.list = list

    def unsplash(self):
        api = "https://source.unsplash.com/1000x1000/?"
        for i in self.list:
            api = api + i + ","
        req =  requests.get(api)
        now = datetime.datetime.now()
        now = now.strftime("%Y_%m_%d_%H_%M_%S_%f") + ".png"
        file = open(now , "wb")
        file.write(req.content)
        file.close()
        return now

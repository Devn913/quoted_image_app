import requests


class Quote:

    def getQuote(self):
        url = "https://api.quotable.io/random"  # Free to use API
        length = 150  # MAX LENGHT OF THE QUOTE
        while True:
            try:
                req = requests.get(url, params={"maxLength": length})
            except:
                return "Something went wrong........!"
                pass
            else:
                break
        quote = req.json().get("content") + " - " + req.json().get("author")
        return quote

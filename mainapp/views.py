from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    if request.method == 'POST':
        quote = getQuote()
        data = {'flag': True, "quote": quote}
        return render(request, 'index.html', context=data)
    else:
        return render(request, 'index.html')


def getQuote():
    url = "https://api.quotable.io/random"  # Free to use API
    length = 150  # MAX LENGHT OF THE QUOTE
    while True:
        try:
            req = requests.get(url, params={"maxLength": length})
        except:
            return "Something went wrong.....! PLEASE TRY AGAIN LATER"
        else:
            break
    quote = req.json().get("content") + " - " + req.json().get("author")
    return quote

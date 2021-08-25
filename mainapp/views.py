from django.shortcuts import render
from edit_image import ImageEdit
import requests

# Create your views here.
def home(request):
    if request.method == 'POST':
        img = ImageEdit()
        url = img.run()
        data = {'flag': True, "url": url}
        return render(request, 'index.html', context=data)
    else:
        return render(request, 'index.html')

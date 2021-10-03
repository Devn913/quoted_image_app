from django.shortcuts import render
from edit_image import ImageEdit
from .models import contactMe


# Create your views here.


def home(request):
    if request.method == 'POST':
        img = ImageEdit()
        url = img.run()
        data = {'flag': True, "url": url}
        return render(request, 'index.html', context=data)
    else:
        return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('mail')
        user_issue = request.POST.get('issue')
        print(user_issue + " " + user_name + " " + user_email)
        data = contactMe(name=user_name, email=user_email, issue=user_issue)

        data.save()
        context = {
            'flag': True
        }
        return render(request, 'contact.html', context=context)

    else:
        return render(request, 'contact.html')

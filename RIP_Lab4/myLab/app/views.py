from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class NewView(View):
    def get(self, request):
        a = 'This is my first Django App'
        linksdict = {
            'links': [
                        {'title': 'first link', 'id': 1, 'information': 'some other information about link'},
                        {'title': 'second link', 'id': 2, 'information': 'some other information about link'},
                        {'title': 'third link', 'id': 3, 'information': 'some other information about link'}
             ]
        }
        return render(request, 'my.html', linksdict)


class ListView(View):
    def get(self, request, id):
        linksdict = {
            'link': {
                'id': id
            }
        }
        return render(request, 'newHtml.html', linksdict)

def goHere(request):
    return HttpResponse('Hi Hi')
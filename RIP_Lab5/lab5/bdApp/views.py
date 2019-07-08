from django.shortcuts import render, HttpResponse
from django.views import View
from bdApp.models import Bottle
# Create your views here.


class BottleView(View):
    def get(self,request):
        objects = Bottle.objects.all()
        return render(request,'index.html',{'obj': objects})

from django.shortcuts import render
from django.views import View
# Create your views here.

class Article(View):
    def get(self,request):
        return render(request,'message/articles.html')
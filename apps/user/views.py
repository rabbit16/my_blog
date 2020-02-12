from django.shortcuts import render
from django.views import View
import logging
from blog  import models
# Create your views here.
logger = logging.getLogger('django')
class Index(View):
    def get(self,request):
        return render(request, 'index/index.html')


# class Intro(View):
#     def get(self,request):
#         pic_t = ContextImage.objects.only('id','name','text','img_url').filter(is_delete=False)
#         return render(request, 'dco/index.html',context={
#             'pic_t':pic_t
#         })
#
class ContextShow(View):
    def get(self,request):
        article = models.Article.objects.filter(is_delete=False)
        return render(request,'message/index.html',context={
            'article':article
        })
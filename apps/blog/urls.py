from django.urls import path
from blog import views
app_name = 'blog'
urlpatterns = [
   path('',views.Article.as_view(), name = 'article')
]
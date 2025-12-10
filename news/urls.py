from django.urls import path
from .views import NewsViews, NewsCreateView
# from .views import news_view


urlpatterns =[
    # path('',news_view,name='news_page')
    path('', NewsViews.as_view(), name='home'),
    path('create/', NewsCreateView.as_view(), name='create')


]
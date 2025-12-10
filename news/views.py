from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import NewsModel
from django.urls import reverse_lazy
from .forms import NewsForm

class NewsViews(ListView):
    model = NewsModel
    template_name = 'index.html'
    context_object_name = 'news'
    ordering = ['-id']

class NewsCreateView(CreateView):
    model =NewsModel
    form_class = NewsForm
    template_name = 'create_news.html'
    success_url = reverse_lazy('home')    


# def news_view (request):
#     new = NewsModel.objects.all()
#     context = {
#         'new':new
#     }
#     return render(request,'index.html',context)

# Create your views here.

from django.shortcuts import render
from django.views import generic
from .models import Articles

# Create your views here.


class ArticleList(generic.ListView):
    queryset = Articles.objects.filter(status=1).order_by('created_on')
    template_name = 'blog/article_list.html'


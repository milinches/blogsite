from django.shortcuts import render
from django.views import generic
from .models import Articles

# Create your views here.


class ArticleList(generic.ListView):
    queryset = Articles.objects.filter(status=1).order_by('created_on')
    context_object_name = 'article_list'
    template_name = 'blog/article_list.html'


class ArticleDetail(generic.DetailView):
    model = Articles
    template_name = 'blog/article_detail.html'


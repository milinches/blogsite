from django.shortcuts import render
from django.views import generic


class HomeView(generic.DetailView):
    template_name = 'home.html'


class AboutView(generic.DetailView):
    template_name = 'about.html'






from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from .models import Post
from django.views import generic
from django.db.models import Q
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# def home(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
    
#     posts = Post.objects.all()[0:5]
    
#     context = {'posts': posts}
    
#     return render(request,'index.html', context)

# def postsPage(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
#     model = Post
#     return render(request, 'post.html', {'model': model})
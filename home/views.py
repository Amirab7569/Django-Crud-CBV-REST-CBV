from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Post
from .forms import CreatePost, UpdatePost
from django.contrib import messages
from django.http import HttpResponse
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response



# ListView : show data from DB
class HomeView(LoginRequiredMixin,ListView):
    '''
    with PermissionRequireMixinis
    permission_required = 'home.view_post'
    '''
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'
       
    
class DetailsView(LoginRequiredMixin,DetailView):
    model = Post
    
'''
class CreatePostView(FormView):
    template_name = 'home/create.html'
    form_class = CreatePost
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = CreatePost
    template_name = 'home/post_create.html'
    success_url = '/'
   
    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)
   
    
class UpdatePostView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'home/update.html' 
    form_class = UpdatePost
    success_url = '/'
    
    
class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/'
    

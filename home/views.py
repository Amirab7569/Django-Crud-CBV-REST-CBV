from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreatePost, UpdatePost
from django.contrib import messages
# Create your views here.


# ListView : show data from DB
class HomeView(ListView):
    model = Post
    template_name = 'home/index.html'
    def get(self, request):
        posts = self.model.objects.all()
        return render(request, self.template_name, {'posts':posts})
    
class DetailsView(DetailView):
    model = Post
    template_name = 'home/details.html'
    def get(self, request, post_id):
        post = self.model.objects.get(pk=post_id)
        return render(request, self.template_name, {'post':post})
    
class CreatePostView(CreateView):
    model = Post
    template_name = 'home/create.html'
    fields = '__all__'
    def post(self, request):
        if request.method == 'POST':
            form = CreatePost(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                Post.objects.create(title=cd['title'], body=cd['body'], author=cd['author'], is_published=cd['is_published'], created=cd['created'])
                messages.success(request,'New Post created', 'danger')
                return redirect('home:index')
        else:
            form = CreatePost()
        return render(request, self.template_name, {'form':form})
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'home/update.html' 
    fields = '__all__'
    
    def post(self, request, pk):
        post = self.model.objects.get(pk=pk)
        if request.method == 'POST':
            form = UpdatePost(request.POST,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,'Post updated Successfully', 'success')
                return redirect('home:index')
        else:
            form = UpdatePost(instance=post)
        return render(request, self.template_name, {'form':form})
    
    
class DeletePostView(DeleteView):
    model = Post
    def get(self, request, pk):
        self.model.objects.get(pk=pk).delete()
        messages.success(request,'Post Deleted Successfully', 'danger')
        return redirect('home:index')
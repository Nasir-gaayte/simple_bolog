from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Category
from .forms import CategoryForm, PostForm 
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


# def home(request):
#     return render(request, 'theblog/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'
    ordering = ['-post_date']
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request,'theblog/category_list.html',{'cats':cats, 'category_posts':category_posts})
   


class Detail(DetailView):
    model = Post
    template_name = 'theblog/deteil.html'


class DetailCategory(DetailView):
    model = Category
    template_name = 'theblog/detail_category.html'       
       
       
    
@login_required    
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            messages.error(request,'wrong')
            return redirect('add_post')
    form = PostForm()
    return render(request,'theblog/add_post.html',{'form':form})    
 

@login_required    
def add_cotegory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            messages.error(request,'wrong')
            return redirect('add_category')
    form = CategoryForm()
    return render(request,'theblog/add_category.html',{'form':form})    
      
       
class UpdatePostView(UpdateView):
    model= Post
    template_name = 'theblog/update_post.html'    
    fields = '__all__'    
    



class DeletePostView(DeleteView):
    model= Post
    template_name = 'theblog/delete_post.html'    
    success_url = reverse_lazy('home')    
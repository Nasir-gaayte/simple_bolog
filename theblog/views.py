from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.


# def home(request):
#     return render(request, 'theblog/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'
    

class Detail(DetailView):
    model = Post
    template_name = 'theblog/deteil.html'   
    
    
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
 
        
        
class UpdatePostView(UpdateView):
    model= Post
    template_name = 'theblog/update_post.html'    
    fields = '__all__'    
    



class DeletePostView(DeleteView):
    model= Post
    template_name = 'theblog/delete_post.html'    
    success_url = reverse_lazy('home')    
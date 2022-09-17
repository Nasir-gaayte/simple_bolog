
from multiprocessing import context
from nntplib import ArticleInfo
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Category,Comment
from .forms import CategoryForm, CommentForm, PostForm ,CommentForm 
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
class CommentView(CreateView):
    model= Comment
    form_class = CommentForm
    # fields = ("name","body")
    template_name= 'theblog/comment.html'
    def form_vaild(self,form):
        form.instance.post.id = self.kwargs['pk']
        return super().form_vaild(form)
     

# def add_comment(request):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = CommentForm()
#     return render(request,'theblog/comment.html',{'form':form})        
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('deteil', args=[str(pk)]))


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
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Detail,self).get_context_data()
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked =True
        
        
        context['cat_menu'] = cat_menu
        context['total_likes']= total_likes
        context['liked']= liked
        return context

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
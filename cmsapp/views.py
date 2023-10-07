

# Create your views here.

# cms_app/views.py

from django.shortcuts import get_object_or_404,render,redirect
from .models import User, Post, Like
from django.contrib.auth import authenticate, login as auth_login
from .models import UserProfile

def user_register(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name,email,password)
        
        user = User.objects.create_user(username=name,email=email, password=password)
        # user_profile, created = UserProfile.objects.get_or_create(user=user)
        
         # Create a UserProfile for the new user
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        
        auth_login(request, user)
        return redirect('login')
    return render(request, 'register.html')
    
    
def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            
            return redirect('home')
    return render(request, 'login.html')
    
    
def home(request):
    print('hello')  
    
    posts = Post.objects.all()
    users = User.objects.all()
    likes = Like.objects.all()
   
    # total_likes = 0
    # for i in likes:
    #     total_likes += 1
    return render(request,'home.html',{'posts': posts,"users":users,'likes':likes})  
    
    
def create_post(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        description = request.POST.get('description')
        is_public = request.POST.get('is_public')
        
        print(title,content,description,is_public)
        print(request.user.userprofile)
        
        post = Post()
        post.title = title
        post.content = content
        post.description = description
        if is_public == 'on':
            post.is_public = True
        else:    
            post.is_public = False
        post.owner = request.user.userprofile   
        
        post.save()
        
        return redirect('home')
        
        
     
    return render(request,'create_post.html')   
            

def create_like(request,post_id):
    print('postid',post_id)
    post = get_object_or_404(Post, pk=post_id)
    user = request.user.userprofile

    # Check if the user has already liked the post
    existing_like = Like.objects.filter(user=user, post=post).first()

    if existing_like:
        # User has already liked the post, so remove the like
        existing_like.delete()
    else:
        # User hasn't liked the post yet, so create a new like
        Like.objects.create(user=user, post=post)

    # return redirect('post-detail', post_id=post_id)  # Redirect to the post detail page
    return redirect('home')


def delete_post(request,post_id):
        # Get the post object to delete
    print(post_id)
    post = get_object_or_404(Post, pk=post_id)
        # Check if the request method is POST (usually from a form submission)
    post.delete()
    return redirect('home')  # Redirect to a view that home posts

  

def update_user(request,user_id):
    print(user_id)
    
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name,email)
        user = User.objects.get(id = user_id)
        
        user.username = name
        user.email = email
        
        user.save()
        
        return redirect('home')
    
    user = User.objects.get(id = user_id)
    print(user)
    return render(request,'update_user.html',{'user':user})


def delete_user(request,user_id):
    print('delete')
    print(user_id)
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('user-list')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

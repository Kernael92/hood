from django.shortcuts import render,redirect
from .models import Profile,Business,Hood,Post,Comment
from django.contrib.auth.models import User
from .forms import NewPostForm,ProfileForm,NewBusinessForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    posts = Post.objects.all()
    return render(request,'hood/home.html',{'posts':posts})

@login_required
def new_post(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES,)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = current_user
            post.save()
        return redirect ('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form': form})

def profile(request,username):
    user = User.objects.get(username=username)
    if not user:
        return redirect('home')
    profile = Profile.objects.get(user=user)
    context = {
        'username':username,
        'user': user,
        'profile': profile,
    }

    return render(request, 'hood/profile.html', context)

@login_required
def profile_setting(request):
    current_user = request.user 
   
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save
            profile.user = current_user
        return redirect(reverse('home'))
        
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'hood/profile_setting.html', context)

@login_required
def business(request):
    business = Business.objects.all()
    return render(request,'hood/business.html', {'business':business})

@login_required
def new_business(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES,)
        if form.is_valid():
            business = form.save(commit = False)
            business.user = current_user
            business.save()
        return redirect ('business')
    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {'form': form})

def search_results(request):
    if 'post' in request.GET and request.GET['post']:
        search_term = request.GET.get('post')
        searched_posts = Post.search_by_hood(search_term)
        message = f"{search_term}"

        searched_posts = Post.search_by_hood(search_term)
        return render(request, 'hood/search.html', {'message':message, 'posts':searched_posts})

    else:
        message = 'You have not searched for any term'
        return render(request, 'hood/search.html', {'message':message})


def post(request,id):
    post = Post.objects.get(pk = id)
    current_user = request.user
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            comment.user = current_user
    else:
        form = CommentForm()

    context = {
        'id':id,
        'post':post,
        'comments':comments,
        'form':form
    }
    return render(request, 'post.html', context)



from django.shortcuts import render,redirect
from .models import Profile,Business,Hood,Post
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required


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





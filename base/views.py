from email.message import Message
from tkinter.messagebox import NO
from django.contrib import messages
import json
from multiprocessing import context
from django.shortcuts import redirect, render
from base.forms import MyUserStartForm
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse


def signup(request):
    form = MyUserStartForm()
    
    if request.method == 'POST':
        form =MyUserStartForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An Error Occored unable to process')
            
    context = {'form': form}
    return render(request, 'base/signup.html', context)
    

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=username)
        except:
            messages.error(request, 'user dosnot exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'password not correct')
            
    context = {}
    return render(request, 'base/loginpage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def homePage(request):
    posts = Blogpost.objects.all()
    context = {'posts': posts}
    
    return render(request, 'base/home.html', context)

def aboutUs(request):
    
    return render(request, 'base/about.html')


def category(request):
    posts = Blogpost.objects.all()
    
    return render(request, 'base/category.html', {'posts': posts})



def postPage(request, pk):
    post = Blogpost.objects.get(id=pk)
    author = User.objects.get(id=pk)
    tags = post.tag.all()
    users = User.objects.all()
    post_comment = post.commentchat_set.all().order_by('-created')
    
    if request.method == 'POST':
        comment = CommentChat.objects.create(
            user = request.user,
            post = post,
            comment=request.POST.get('body')
        )
        return redirect('postpage', pk=post.id)
    
    context = {'post': post, 'tags': tags, 'post_comment':post_comment, 'author':author}
    return render(request, 'base/postpage.html', context)


def deleteComment(request):
    data = json.loads(request.body)
    userId = data['userId']
    commentId = data['commentId']
    print('userid:', userId)
    print('commentid:', commentId)
    
    
    comment = CommentChat.objects.get(id=commentId)
    user = User.objects.get(id=userId)
    
    if user != comment.user:
        print('deleted not working')
        return JsonResponse('cannot delete not your message', safe=False)
        
        
        
    if request.method == 'POST':
        comment.delete()
        print('deleted')
    
    return JsonResponse('deleted comment', safe=False)
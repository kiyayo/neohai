from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import mail_admins
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,render
from itertools import chain
from main.forms import EntryForm,ProfileForm,CommentForm,FeedbackForm
from main.models import Entry,Star,Gallery


def index(request):
    entries = Entry.objects.all().order_by('-created_at')[:12]
    if request.method == 'POST':
        form = EntryForm(request.POST)
        comment = CommentForm(request.POST)
        if form.is_valid or comment.is_valid:
           form.save()
           comment.save()
           messages.success(request,'Your entry has been posted successfully!')
        else:
            print(form.errors)     
    else:
        comment = CommentForm()
        form = EntryForm()  
    return render(request,'main/index.html',{'form':form,'entries':entries,'comment':comment})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_profile = ProfileForm(request.POST,request.FILES)
        if form.is_valid() and user_profile.is_valid():
           form.save()
           return redirect('/login')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
        user_profile = ProfileForm()
    return render(request,'main/register.html',{'form': form,'user_profile': user_profile})  

@login_required
def profile(request):
    return render(request, 'main/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile) 
        if  profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Your profile has been updated successfully!')
            return redirect('/profile')
    else:
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render (request,'main/edit_profile.html', {'profile_form': profile_form})

def username(request,username):
    user = get_object_or_404(User,username=username)
    entry_list = Entry.objects.filter(user=user)
    paginator = Paginator(entry_list,12)
    page = request.GET.get('page')
    entries = paginator.get_page(page)
    return render(request,'main/username.html',{'entries':entries})

def keyword(request,keyword):
    entry_list = Entry.objects.filter(keyword=keyword).order_by('-created_at')
    paginator = Paginator(entry_list,12)
    page = request.GET.get('page')
    entries = paginator.get_page(page)
    return render(request,'main/keyword.html',{'entries':entries})

def about(request):
    return render(request,'main/about.html')


def star(request,pk):
    if request.method == 'POST' and request.is_ajax():
       user = request.user
       entry = get_object_or_404(Entry,pk=pk) 
       star = Star.objects.create(user=user,entry=entry) 
       return JsonResponse({'sucess':'true'})
    

def search(request):
        query = request.GET.get('search')
        entry_list = Entry.objects.filter(keyword__icontains=query)
        paginator = Paginator(entry_list,12)
        page = request.GET.get('page')
        entries = paginator.get_page(page)
        return render(request,'main/search.html',{'entries':entries})



def starred(request):
    starred_list = userprofile.stars.all().order_by('-created_at')
    paginator = Paginator(favourite_list,12)
    page = request.GET.get('page')
    starred_entries = paginator.get_page(page)
    return render(request,'main/starred.html',{'starred_entries':starred_entries})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            mail_subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            subject=category +':'+''+mail_subject
            mail_admins(subject,message)
            messages.success(request,'Your feedback has been sent to the admins')
        else:
            print(form.errors)
    else:
        form = FeedbackForm()
    return render(request,'main/feedback.html',{'form':form})

        
def gallery(request):
    photo_list = Gallery.objects.all().order_by('-timestamp')
    paginator = Paginator(photo_list,12)
    page = request.GET.get('page')
    photos = paginator.get_page(page)
    return render(request,'main/gallery.html')


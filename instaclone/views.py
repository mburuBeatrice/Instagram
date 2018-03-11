from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Post,Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm,ProfileForm
from django.contrib import messages
# Create your views here.
@login_required(login_url='/accounts/login/')   
def post_list(request):

    queryset = Post.objects.all()

    context = {
        "object_list": queryset,
        "name": "List"    }

    return render(request, 'post_list.html', context)
@login_required(login_url='/accounts/login/') 
def post_detail(request, id):

    instance = get_object_or_404(Post,id=id)
    context = {
    "name": instance.name,
    "instance" : instance
    }
    return render(request, 'post_detail.html', context)
@login_required(login_url='/accounts/login/') 
def post_create(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not successfully created")


    context = {
        "form" : form,
    }

    return render(request, 'post_form.html', context)


@login_required(login_url='/accounts/login/') 
def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
   

    context = {
    "name": instance.name,
    "instance": instance,
    "form": form,
    }
    return render(request, 'post_form.html', context)
@login_required(login_url='/accounts/login/') 
def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post Deleted")
    return redirect("post_list")
   

# def get_post_by_id(request):
#     
#     posts = Post.objects.all()

#     return render(request, 'post_list.html',{"posts":posts})


    
    
# @login_required(login_url='/accounts/login/')        
# def profile(request):
   
#     return render(request,"profile.html", {"profile":profile})
# @login_required(login_url='/accounts/login/')
# def new_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.image = current_user
#             profile.save()
#     else:
#         form = NewProfileForm()
#     return render(request, 'new_profile.html', {"form": form})    
@login_required(login_url='/accounts/login/')   
def profile_list(request):

    queryset = Profile.objects.all()

    context = {
        "prof_list": queryset,
          }

    return render(request, 'profile_list.html', context)   
@login_required(login_url='/accounts/login/') 
def profile_detail(request, id):

    insta = get_object_or_404(Profile,id=id)
    context = {
    "bio": insta.bio,
    "insta" : insta
    }
    return render(request, 'profile_detail.html', context)
@login_required(login_url='/accounts/login/') 
def profile_create(request):

    form = ProfileForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        insta = form.save(commit=False)
        insta.save()
        # messages.success(request, "Profile Successfully created")
        return HttpResponseRedirect(insta.get_absolute_url())
    else:
        # messages.error(request, "Profile Not successfully created")


        context = {
            "form" : form,
        }

    return render(request, 'profile_form.html', context)

@login_required(login_url='/accounts/login/') 
def profile_update(request, id=None):
    insta = get_object_or_404(Profile, id=id)
    form = ProfileForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        insta = form.save(commit=False)
        insta.save()
        messages.success(request, "Profile Saved")
        return HttpResponseRedirect(insta.get_absolute_url())
   

    context = {
    "bio": insta.bio,
    "insta": insta,
    "form": form,
    }
    return render(request, 'profile_form.html', context)
@login_required(login_url='/accounts/login/') 
def profile_delete(request, id=None):
    insta = get_object_or_404(Profile, id=id)
    insta.delete()
    messages.success(request, "Profile Deleted")
    return redirect("instaclone:profile_list")
   
def find_profile(name):
    pass   


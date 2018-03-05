from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm
# Create your views here.
def welcome(request):

    images = Image.objects.all()
    return render(request, 'welcome.html',{"images":images})

    
@login_required(login_url='/accounts/login/')        
def profile(request,profile_id):
    try:
        profile = Profile.objects.get(id = profile_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"profile.html", {"profile":profile})
@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.image = current_user
            profile.save()
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})    
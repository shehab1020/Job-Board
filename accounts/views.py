from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import Signup, ProfileForm, UserForm
from django.contrib.auth import authenticate, login
from . models import Profile
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect(reverse('profile'))
    else:
        form = Signup()
    context = {'form':form}
    return render(request, 'registration/signup.html',context)


def profile(request):
    profile = request.user
    user = Profile.objects.get(user=profile)
    context = {'profile':user}
    return render(request, 'accounts\profile.html',context)

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            my_profile_form = profileform.save(commit=False)
            my_profile_form.user = request.user
            my_profile_form.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    context = {'profile':profile,'userform':userform, 'profileform': profileform}
    return render(request,'accounts/profile_edit.html',context)
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def home_view(request):
    return render(request, 'notes/home.html')

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('notes/login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/notes/loggedin/')
    else:
        return HttpResponseRedirect('/invalid_login')

def loggedin(request):
    return render_to_response('notes/loggedin.html',
                              {'full_name' : request.user.username})
def invalid_login(request):
    return render_to_response('notes/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('notes/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/notes/loggedin/')
    else:
            form = UserCreationForm()

            args = {'form':form}
            return render_to_response(request, 'notes/reg_form.html',args)


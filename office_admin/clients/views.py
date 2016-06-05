from django.shortcuts import redirect, render_to_response
from .forms import RegistrationForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from django.contrib.auth.models import User

def login(request):
    return render_to_response('login.html')

def logout_page(request):
    logout(request)
    return redirect('clients:login')

def profile(request):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return HttpResponseRedirect('/admin')
        else:
            user = User.objects.get(username=request.user.username)
    else:
        user = None
    return render_to_response(
                              'profile.html',
                              { 'user': user }
                              )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'])
            user.save()
            return redirect('clients:profile')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
                            'form': form})
    
    print 'render to response'
    return render_to_response(
                'registration/register.html', variables)
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form=userform(request.POST)
			if form.is_valid():
				username=form.cleaned_data['username']
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				email = form.cleaned_data['email']
				password = form.cleaned_data['password']
				User.objects.create_user(username=username,
				first_name=first_name,last_name=last_name,
				email=email,password=password)
				return redirect('login')
		else:
			form = userform()
			context = {'form':form}
		return render(request, 'home.html', context)
	else:
		return render(request, 'index.html')
	
def login_user(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return render(request, 'index.html')
			else:
				return HttpResponse('<h1>invalid</h1>')    
		return render(request, 'login.html')
	else:
		return render(request,'index.html')    
		
def logout_user(request):
	logout(request)
	return render(request,'login.html')    

def changepassword(request):
	if request.method == 'POST':
		pass
	else:
		form = ChangePasswordForm()
	return render(request, 'changepass.html',{'form':form})	
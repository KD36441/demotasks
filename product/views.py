from django.shortcuts import render
from itertools import product
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission

# Create your views here.
from .models import *
from .forms import productForm, CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for '+user )

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	return render(request, 'accounts/dashboard.html')


@login_required(login_url='login')
def getproduct(request):
	if request.method=='POST':
		fm=productForm(request.POST)
		if fm.is_valid():
			fm.save()
	else:
		fm=productForm()
		return render(request,'accounts/dashboard.html',{'form':fm})
		 


@login_required(login_url='login')
def createproduct(request, pk):
	product = Product.objects.get(id=pk)
	form = productForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def updateproduct(request, pk):

	product = Product.objects.get(id=pk)
	form = productForm(instance=product)

	if request.method == 'POST':
		form = productForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/')

		context = {'form':form}
		return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def deleteproduct(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('/')

	context = {'item':product}
	return render(request, 'accounts/delete.html', context)



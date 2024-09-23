from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# User Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})  # Render signup form

# User Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
    return render(request, 'blog/login.html')  # Render login page

# User Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Home Page View
@login_required(login_url='login')  # This ensures users are redirected to login if not authenticated
def home_view(request):
    return render(request, 'blog\home.html')

# Blog Page View
@login_required  # Ensures that the user must be logged in to access the blog page
def blog_view(request):
    return render(request, 'blog/blog.html')  # Render blog page

# About Creator Page View
def about_view(request):
    return render(request, 'blog/about.html')  # Render about page

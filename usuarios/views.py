from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from products.models import Product

# Create your views here.

def home_view(request):
    context = {}
    
    context["products"] = Product.objects.all()

    return render(request, 'home.html', context=context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home') 

def login_view(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if (user is not None):
            login(request, user)
            return redirect('home') 
        
        return render(request, 'login.html',{'error': 'Credenciales incorrectas, vuelta a intentarlo'})
    
    return render(request, 'login.html')

def register_view(request):
    
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
    
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')
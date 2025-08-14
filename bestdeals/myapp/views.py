from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flipkart, Amazon, User

# Home View
def home_view(request):
    return render(request, 'home.html')

# About View
def about_view(request):
    return render(request, 'about.html')

# Contact View
def contact_view(request):
    return render(request, 'contact.html')

# Product Comparison View
@login_required
def comparison_view(request):
    product_name = request.GET.get("product_name", "").strip()

    # Fetch product data from Flipkart and Amazon tables
    amazon_product = Amazon.objects.filter(product_name__iexact=product_name).first()
    flipkart_product = Flipkart.objects.filter(product_name__iexact=product_name).first()

    # Render the compare.html template with results
    return render(request, "compare.html", {
        "search_query": product_name,
        "amazon_product": amazon_product,
        "flipkart_product": flipkart_product
    })

# User Authentication Views
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if not username or not email or not password:
            messages.error(request, "All fields are required!")
            return redirect('user_signup')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('user_signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('user_signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('user_signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        return redirect('user_login')

    return render(request, 'userregister.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Username and Password are required!")
            return redirect('user_login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('comparison')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('user_login')

    return render(request, 'userlogin.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Admin Login View
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session["admin_authenticated"] = True  # Set session
            return redirect("admin_dashboard")
        else:
            return render(request, "adminlogin.html", {"error": "Invalid credentials!"})

    return render(request, "adminlogin.html")

# Admin Dashboard View
def admin_dashboard(request):
    if not request.session.get("admin_authenticated"):
        return redirect("admin_login")

    return render(request, "admindash.html")

# Admin Logout View
def admin_logout(request):
    request.session.pop("admin_authenticated", None)  # Remove session
    return redirect("admin_login")


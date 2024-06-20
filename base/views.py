from django.shortcuts import render, redirect
from .models import Donations

def home(request):
    return render(request, 'base/home.html')

def support(request):
    return render(request, 'base/support.html')

def about(request):
    return render(request, 'base/about.html')

def donations(request):
    return render(request, 'base/donations.html')

def donations_success(request):
    return render(request, 'base/donations_success.html')

def submit_donation(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        message = request.POST.get('message')

        # Here, you would typically save the data to the database or process it as needed

        # Redirect to the success page after processing
        return redirect('donations_success')

    # If not a POST request, redirect to the donations page
    return redirect('donations')

def adoption(request):
    return render(request, 'base/adoption.html')
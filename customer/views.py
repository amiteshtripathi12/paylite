from django.shortcuts import render


def home(request):
    return render(request, 'customer/home.html')
# Create your views here.

from django.shortcuts import render

# Create your views here.

def site(request):
    return render(request, 'home/index.html')
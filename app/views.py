from django.shortcuts import render

# Create your views here.

def roommates(request):
    return render(request,'roommates.html')

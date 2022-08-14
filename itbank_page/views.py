from django.shortcuts import render

# Create your views here.
def home(req):
    

    return render(req,'home/home.html')

def dolar(req):
    return render(req,'home/dolar.html')
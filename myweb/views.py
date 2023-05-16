import html
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,'reach.html')
def test(request):
    return render(request,'test.html')
def tiao(request):
    return render(request,'tiao.html')
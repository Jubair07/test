from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render (request,'a.html',{'title':'Django','link':'https://www.youtube.com/'})

def profile(request):
    return HttpResponse ("profile page")

def update(request):
    return HttpResponse ("update page")

def expression(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    return render(request,'output.html',{'result': c})
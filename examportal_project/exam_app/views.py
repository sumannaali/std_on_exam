from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
    #return render(request,'exam\login.html')

#def home(request):
    #return render(request,'exam/register.html')

def home(request):
    return render(request,'exam/dashboard.html')  
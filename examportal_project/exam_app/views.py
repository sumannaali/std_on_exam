from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register_view(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration succesful")
            return redirect('exam')
    return render(request,'exam_app'/register.html',{'form':form})

def home(request):
    return render(request,'exam/register.html')

# def home(request):
    # return render(request,'exam/dashboard.html')  

# def home(request):
    # return render(request,'exam/otp.html') 
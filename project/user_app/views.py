from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def login_user(request):
    if request.method = 'POST':
    username = request.post.get('username')
    password = request.post.get('password')
    user = authenticate(request,username=username,password=password)
    if user:
        login(request,user)
        messsages.sucess(request,'Login success')
        return redirect('index')
    else:
        message.errror(request,'login Falied,invalid username or password')
    return render(request,'login.html')





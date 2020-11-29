from django.shortcuts import render
from .models import PhotoCrypto, User
from django.http import HttpResponse
import hashlib

def Login(request):
    if(request.method == "POST"):
        photos = PhotoCrypto.objects.all()
        result = generate_pass(request,photos)
        password = ''
        if(len(result) < 4):
            return HttpResponse('Password shoud be atleast 4 images')
        username = request.POST.get('username')
        if(validate_user(username)):
            for i in result:
                password += hash_password(i)
            user = User.objects.get(username = username)
            if(user.photo_password == password):
                return HttpResponse('You logged in successfully')

    return render(request,'main/Login.html')
# Function which handles Signup requests
def Signup(request):
    photos = PhotoCrypto.objects.all()
    context = {
    'photos' : photos
    }
    password = ''
    if(request.method == "POST"):
        result = generate_pass(request, photos)
        if(len(result) < 4):
            return HttpResponse('Password shoud be atleast 4 images')
        username = request.POST.get('username')
        if(validate_user(username)):
            return HttpResponse('Username is already taken')
        for i in result:
            password += hash_password(i)
        user = User(username = username, firstname = request.POST.get('first'),
        lastname = request.POST.get('last'),photo_password = password)
        user.save()
    return render(request,'main/Signup.html', context)

def validate_user(username):
    is_user = User.objects.filter(username = username)
    if len(is_user) == 1:
        return True
    return False

def hash_password(password):
    lib = hashlib.sha512(password.encode())
    return str(lib.digest())

def generate_pass(request, photos):
    result = []
    for i in photos :
        if request.POST.get(i.photo_name):
            result.append(i.photo_name)
    return result

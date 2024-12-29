from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from users.models import User
from services.models import File

from utils.helpers import update_verification_link


def home(request):
    if not request.user.is_authenticated:
        return redirect('login/')
    template = 'users/home.html'
    context = {'file_list': File.objects.filter(
        is_active=True).order_by('-uploaded_at')}
    return render(request, template, context=context)


def user_signup(request):
    template = 'users/signup.html'
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            context['message'] = 'This email is already registered with another user.'
        else:
            try:
                user = User.objects.create_user(email=email, password=password)
                update_verification_link(user)
                context['message'] = 'Verification email has been sent. Please check your inbox.'
            except Exception as ex:
                print("Exception occurred:", ex)
                context['message'] = 'Something went wrong. Please try again.'
    return render(request, template_name=template, context=context)



def user_login(request):
    template = 'users/login.html'
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user,
                  backend='users.backends.EmailAuthentication')
            return redirect('/')
        else:
            context['message'] = "Either email is not valid or user is not registered"
    return render(request, template_name=template, context=context)

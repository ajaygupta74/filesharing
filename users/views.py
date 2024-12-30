from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from django.http import HttpResponse
from users.models import User
from services.models import File

from utils.helpers import send_verification_mail


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
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            context['message'] = 'This email is already registered with another user.'
        else:
            try:
                verify_token = send_verification_mail(email)
                user = User.objects.create_user(email=email, password=password)
                user.email_verification_link = verify_token
                user.save(update_fields=['email_verification_link'])
                context['message'] = 'Verification email has been sent. Please check your inbox.'
            except Exception as ex:
                print("Exception occurred:", ex)
                context['message'] = 'Something went wrong. Please try again.'
    return render(request, template_name=template, context=context)


def user_verify_email(request, token):
    user = get_object_or_404(User, email_verification_link=token)
    context = {}
    if user.email_confirmed:
        context['message'] = "Email already verified"
    else:
        user.email_confirmed = True
        user.save(update_fields=['email_confirmed'])
    return redirect('/login/')
    

def user_login(request):
    template = 'users/login.html'
    context = {}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        if not user:
            context['message'] = "Either email is not valid or user is not registered"
        elif not user.email_confirmed:
            context['message'] = "Email is not confirmed yet"
        elif not user.check_password(password):
            context['message'] = "Incorrect password"
        else:
            login(request, user)
            return redirect('/')
    return render(request, template_name=template, context=context)

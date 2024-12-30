from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import home, user_login, user_signup, user_verify_email


urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('signup/', user_signup, name='user_signup'),
    path('users/email/verify/<str:token>/', user_verify_email, name='verify_email'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
]
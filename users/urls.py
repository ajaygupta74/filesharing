from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import home, user_login, user_signup


urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('signup/', user_signup, name='user_signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
]
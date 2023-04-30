from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from users.views import RegistrationView, UserLoginView, ProfileView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(ProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]

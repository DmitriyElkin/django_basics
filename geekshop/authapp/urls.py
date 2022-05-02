from django.urls import path

from authapp.views import LoginView, RegisterView, LogoutView, ProfileView

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]

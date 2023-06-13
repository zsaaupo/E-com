from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('account/signup/', views.sign_up, name='signup')
]

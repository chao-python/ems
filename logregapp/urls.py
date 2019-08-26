from django.urls import path
from logregapp import views

app_name = 'logregapp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('loginlogic/', views.loginlogic, name='loginlogic'),
    path('regist/', views.regist, name='regist'),
    path('registlogic/', views.registlogic, name='registlogic'),
    path('getcaptcha/', views.getcaptcha, name='getcaptcha'),
    path('checkname/', views.checkname, name='checkname'),
    path('checkpwd/', views.checkPassword, name='checkpwd'),
    path('caplogic/', views.checkcap, name='checkpcap'),
]

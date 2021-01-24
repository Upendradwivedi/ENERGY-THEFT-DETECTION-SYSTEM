from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("theft.herokuapp.com",views.index ,name="home"),
    path("theft.herokuapp.com/login/home",views.index ,name="home"),
    path("theft.herokuapp.com/login/userinfo",views.user_info,name="userinfo"),
    path("theft.herokuapp.com/login/bill_prediction",views.register,name="register"),
    path("theft.herokuapp.com/login/actual_bill",views.actual_bill,name="actual_bill"),
    path("login/suspect",views.suspect,name="suspect"),
    path("theft.herokuapp.com/login",views.loginuser,name='login'),
    path('theft.herokuapp.com/logout',views.logout_user,name='logout'),
    
]

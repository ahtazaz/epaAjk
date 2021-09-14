from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
   
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('post', views.blogs, name="post"),
    path('getnews', views.newsdata, name="getnews"),
    path('slider', views.slider, name="slider"),
    path('logout',views.logout_user,name="logout"),
    path('login',views.login_user,name="login"),
    path('water', views.water, name="water"),
    path('air', views.air, name="air"),
    path('getair', views.airdata, name="getair"),
    path('getwater', views.waterdata, name="getwater"),
]
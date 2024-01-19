from django.contrib import admin
from django.urls import path
from ecomm_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact',views.contact),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('myview',views.SimpleView.as_view()),
    path('hello',views.hello),
    path('home',views.home),
    path('pdetails',views.pdetails),
    path('register',views.register),
    path('login',views.login)
    ]
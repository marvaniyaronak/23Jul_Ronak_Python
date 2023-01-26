from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.getdata),
    path('get_uid/<int:id>/', views.get_uid),
    path('savedata/', views.savedata),
    path('updatedata/<int:id>/', views.updatedata),
    path('deletedata/<int:id>/', views.deletedata),

]

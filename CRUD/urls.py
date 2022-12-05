from django.urls import path
from . import views

urlpatterns=[
    path('', views.addShow , name='kuch'),
    path('delete/<int:id>/', views.deleteUser , name='deletedata'),
    path('<int:id>/', views.updateUser , name='updatedata')


]
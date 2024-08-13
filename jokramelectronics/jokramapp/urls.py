from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task,name='add_task'),
    path('add_list/', views.add_list, name='add_list'),

]
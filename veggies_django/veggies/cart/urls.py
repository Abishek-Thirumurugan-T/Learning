#created module
from django.urls import path
from . import views #for relative same folder path . is used

urlpatterns = [
    path('', views.home, name='home'),
   path('cartcreate/', views.cache_create),
    path('cartread/', views.cache_read),
    path('cartdelete/', views.cache_delete), ]
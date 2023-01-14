from django.urls import path
from . import views #for relative same folder path . is used

urlpatterns = [
    path('runvideo/', views.run_video),
    path('classes/', views.classes),
    path('add/', views.add_db),
    path('delete/', views.delete_db),
    path('live/', views.livefe),]
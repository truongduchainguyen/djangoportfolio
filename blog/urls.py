from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_blogs, name='home'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
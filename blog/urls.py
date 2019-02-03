from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import projects.views
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]

"""
URL configuration for campusconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('events/', views.events, name='events'),
    path('announcements/', views.announcements, name='announcements'),
    path('clubs/', views.clubs, name='clubs'),
    path('coding/', views.coding, name='coding'),
    path('create-post/', views.create_post, name='create_post'),
    path('like-post/<int:post_id>/', views.like_post, name='like_post'),
    path('add-comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('join-coding/', views.join_coding, name='join_coding'),
    path('cultural/', views.cultural, name='cultural'),
    path('join-cultural/',views.join_cultural,name='join_cultural'),
    path('sports/', views.sports, name='sports'),
    path('literary/', views.literary, name='literary'),
    path('robotics/', views.robotics, name='robotics'),
    path('join-sports/', views.join_sports, name='join_sports'),
    path('join-literary/', views.join_literary, name='join_literary'),
    path('join-robotics/', views.join_robotics, name='join_robotics'),
]

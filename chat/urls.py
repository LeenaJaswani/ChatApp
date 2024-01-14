from django.urls import path
from . import views

urlpatterns = [
  
    path("", views.chat, name="chat"),
     path("chat/<str:pk>", views.chat, name="chat"),
     path('sent_msg/<str:pk>',views.sentMessages,name="sent_msg"),
     path('rec_msg/<str:pk>',views.receivedMessages,name="rec_msg"),
      path('notification/',views.chatNotification,name="notification"),
      path('signup', views.signUpView, name='signup'),
      path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
   
    path('fetch_friends', views.fetch_friends, name='fetch_friends'),
    
path('delete_message/<int:pk>/', views.delete_message, name='delete_message'),


]


from django.urls import path
from hmsapp import views

urlpatterns = [
  path('', views.index, name='index'),
  path('email', views.email, name='email'),
  path('chat', views.chat, name='chat'),
  path('file', views.file, name='file'),
  path('contact', views.contact, name='contact'),
  path('todo', views.todo, name='todo'),
  path('invoice', views.invoice, name='invoice'),
  path('calender', views.calender, name='calender'),
   path('backend', views.backend, name='backend'),
  
]
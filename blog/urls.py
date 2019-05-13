from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.hello_forms, name='hello_forms'),
    path('handle_forms/', views.handle_forms, name='handle_forms')
]

from django.urls import path
from helloapp import views

urlpatterns = [
    path('hello/',views.hello)
]
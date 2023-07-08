from django.urls import path
from .views import index
from django.shortcuts import redirect


def post_view(request):
    return redirect('/127.0.0.1/lesson_4/')

urlpatterns = [
    path('', index)
]
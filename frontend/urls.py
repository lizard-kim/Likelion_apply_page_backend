from django.urls import path
from .views import main, apply

urlpatterns = [
    path('', main, name="main"),
    path('apply/', apply, name="apply"),
]
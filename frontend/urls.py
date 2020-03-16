from django.urls import path
from .views import main, apply, login, admin


urlpatterns = [
    path('', main, name="main"),
    path('apply/', apply, name="apply"),
    path('login/', login, name='login'),
    path('adminpage/', admin, name="admin"),
]

from backend_test.menu import views
from django.urls import path, include

urlpatterns = [
    path('', views.MenuViewAPI.as_view()),
]

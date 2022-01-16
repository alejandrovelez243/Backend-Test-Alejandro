from backend_test.menu import views
from django.urls import path, include

urlpatterns = [
    path('', views.MenuViewMixin.as_view()),
]

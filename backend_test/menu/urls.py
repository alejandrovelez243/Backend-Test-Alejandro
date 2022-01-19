from django.urls import path

from backend_test.menu import views

urlpatterns = [
    path("", views.MenuViewAPI.as_view()),
    path("<int:pk>", views.MenuViewRetrieveAPI.as_view()),
    path("products", views.ProductViewAPI.as_view()),
    path("products/<int:pk>", views.ProductViewRetrieveAPI.as_view()),
]

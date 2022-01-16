from backend_test.staff import views
from django.urls import path, include

urlpatterns = [
    path('', views.StaffViewAPI.as_view()),
    path('order', views.OrderViewAPI.as_view())
]

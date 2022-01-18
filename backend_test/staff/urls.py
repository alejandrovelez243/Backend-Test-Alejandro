from backend_test.staff import views
from django.urls import path, include


app_name = 'staff'
urlpatterns = [
    path('', views.StaffViewAPI.as_view()),
    path('order/<str:uuid>', views.OrderViewAPI.as_view(), name='order')
]

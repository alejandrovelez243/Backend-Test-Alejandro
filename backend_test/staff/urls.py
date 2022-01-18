from backend_test.staff import views
from django.urls import path, include


app_name = 'staff'
urlpatterns = [
    path('', views.StaffViewAPI.as_view()),
    path('order/<str:uuid>', views.OrderRetrieveViewAPI.as_view(), name='order'),
    path('order/', views.OrderListViewAPI.as_view(), name='orderList'),
]

from django.urls import path

from backend_test.staff import views

app_name = "staff"
urlpatterns = [
    path("", views.StaffViewAPI.as_view()),
    path("<int:pk>", views.StaffViewRetrieveAPI.as_view()),
    path("order/<str:uuid>", views.OrderRetrieveViewAPI.as_view(), name="order"),
    path("order/", views.OrderListViewAPI.as_view(), name="orderList"),
]

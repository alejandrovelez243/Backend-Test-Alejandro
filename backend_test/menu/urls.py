from backend_test.menu import views
from django.urls import path

urlpatterns = [
    path('', views.test_slack_message)
]

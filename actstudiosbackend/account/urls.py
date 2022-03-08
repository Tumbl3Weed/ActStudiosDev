from django.urls import path
from account import views
urlpatterns = [
    path('Account/', views.modelCRUD),
]

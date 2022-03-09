from django.urls import path
from account import views
urlpatterns = [
    path('Account/', views.modelCRUD),
    path('School/', views.modelCRUD),
    path('Teacher/', views.modelCRUD),
    path('Student/', views.modelCRUD),
    path('Account/<int:pk>/', views.modelCRUDpk),
    path('School/<int:pk>/', views.modelCRUDpk),
    path('Teacher/<int:pk>/', views.modelCRUDpk),
    path('Student/<int:pk>/', views.modelCRUDpk),
]

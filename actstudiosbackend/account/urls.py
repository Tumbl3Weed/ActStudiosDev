from django.urls import path
from account import views
urlpatterns = [
    path('Account/', views.modelCRUD),
    path('School/', views.modelCRUD),
    path('Teacher/', views.modelCRUD),
    path('Student/', views.modelCRUD),
]

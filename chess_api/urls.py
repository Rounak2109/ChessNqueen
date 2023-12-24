from django.urls import path
from chess_api import views

urlpatterns = [
    path('chess/<str:slug>/', views.output),
    path('chess/',views.hello)
]

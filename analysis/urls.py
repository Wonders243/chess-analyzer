from django.urls import path
from .views import analyze_pgn

urlpatterns = [
    path('', analyze_pgn, name='analyze_pgn'),
]
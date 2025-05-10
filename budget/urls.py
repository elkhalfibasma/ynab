from django.urls import path

from . import views
from .views import budget

urlpatterns = [
    path("budget/", views.budget, name="budget"),
    
    path("delete_item/<int:user_id>", views.delete_item, name="delete-item"),
    path('ajout/', views.ajout, name='ajout'),
]

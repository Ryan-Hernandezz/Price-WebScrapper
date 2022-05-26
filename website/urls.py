from django.urls import path
from website import views

urlpatterns = [
    path('', views.website, name = 'website'),
    path('form/', views.search_item, name = "form"),
]


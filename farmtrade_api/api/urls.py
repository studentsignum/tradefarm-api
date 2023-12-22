from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('profile/', views.UserProfileList.as_view()),
    path('profile/<int:pk>/', views.UserProfileDetail.as_view()),
    path('product/', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
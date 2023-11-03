from django.urls import path

from .views import BookAPIView

urlpatterns = [
    path('api/books/', BookAPIView.as_view(), name='book_list'),
]
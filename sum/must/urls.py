from django.urls import path
from .views import *

urlpatterns = [
    path('reviews/', reviews_view, name='reviews_view'),
    path('review/<int:pk>', review_view, name='review_view'),
]
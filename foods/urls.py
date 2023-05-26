from django.urls import path
from foods.views import FoodListAPIView
from .views import home
from .views import categories


urlpatterns = [
    path('', home, name='home'),
    path('api/foods/', FoodListAPIView.as_view(), name='food-list'),
    path('categories/', categories, name='categories'),
]



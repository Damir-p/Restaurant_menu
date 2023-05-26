from django.shortcuts import render
from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer
from django.shortcuts import render
from .models import Category

class FoodListAPIView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    from django.shortcuts import render

def home(request):
    return render(request, 'base.html')


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

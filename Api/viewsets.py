from rest_framework import viewsets
from Api.models import Pizza
from .serializers import PizzaSerializer
from . import serializers
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import SearchFilter


class PizzaFilter(filters.FilterSet):
    class Meta:
        model = Pizza
        fields = {
            'pizza_type': ['icontains'],
        }
class Pizzas(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    filterset_class = PizzaFilter


class PizzaViewset(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = serializers.PizzaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['pizza_type']


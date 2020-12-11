from django.shortcuts import render
from rest_framework import generics
from . import serializers
from django.shortcuts import get_object_or_404
from .models import Pizza
from .serializers import PizzaSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response


class PizzaFilter(filters.FilterSet):
    class Meta:
        model = Pizza
        fields = {
            'pizza_type': ['icontains'],
        }


def home(request):
    pizza_data = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizza_data})


class Pizzas(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    filterset_class = PizzaFilter

class PizzaViewset(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = serializers.PizzaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['pizza_type']


class Pizzalist(generics.ListAPIView):
    model = Pizza
    serializer_class = PizzaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['pizza_type']

    def get(self, request):
        pizza = Pizza.objects.all()
        serializer = PizzaSerializer(pizza, many=True)
        return Response(serializer.data)


    def get_queryset(self):
        var = self.kwargs['Pizza']
        queryset = self.model.objects.filter(pizza_type=Pizza)
        return queryset

from rest_framework import serializers
from Api.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        extra_kwargs = {'size': {'required': True}}
        fields = '__all__'

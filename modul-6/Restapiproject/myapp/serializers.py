from rest_framework import serializers
from .models import book_model




class book_serializer(serializers.ModelSerializer):
    class Meta:
        model = book_model
        fields = '__all__'

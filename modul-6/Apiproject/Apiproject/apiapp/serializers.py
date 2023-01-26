from rest_framework import serializers
from .models import user_info

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=user_info
        fields='__all__'

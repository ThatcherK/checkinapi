from rest_framework.serializers import ModelSerializer
from .models import Visitor, Register

class VisitorSerializer(ModelSerializer):
    class Meta:
        model=Visitor
        fields=['name', 'company', 'identification_number', 'telephone_number', 'date', 'id']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=Register
        fields=[ 'temperature', 'date']
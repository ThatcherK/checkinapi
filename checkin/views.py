from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer, VisitorSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Register, Visitor
from rest_framework.permissions import IsAuthenticated

class RegisterList(GenericAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

class VisitorList(GenericAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [IsAuthenticated]

class AddVisitor(GenericAPIView):
    serializer_class = VisitorSerializer
    def post(self, request):
        data = request.data
        name = data.get('name')
        company = data.get('company')
        temperature = data.get('temperature')
        identification_number = data.get('identification_number')
        telephone_number = data.get('telephone_number')
        visitor = Visitor.objects.get(name=name)
        if visitor:
            return Response({'message': 'This name already exists'})
        serializer = VisitorSerializer(visitor)
        if serializer.is_valid():
            serializer.save()
            data = {
            'visitor': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RegisterVisitor(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        data = request.data
        visitor = data.get('visitor')
        temperature = data.get('temperature')
        registered_visitor = Register(visitor=visitor, temperature=temperature)
        serializer = RegisterSerializer(registered_visitor)
        if serializer.is_valid():
            serializer.save()
            data = {
                'registered_visitor': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
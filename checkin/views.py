from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from .serializers import RegisterSerializer, VisitorSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Register, Visitor
from rest_framework.permissions import IsAuthenticated


class AddVisitor(ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    def post(self, request):
        data = request.data
        name = data.get('name')
        company = data.get('company')
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
        
class RegisterVisitor(ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    def post(self, request):
        post_data = request.data
        visitor = post_data.get('visitor')
        temperature = post_data.get('temperature')
        data = {
            'visitor': visitor,
            'temperature': temperature
        }
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'registered_visitor': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateAPIView
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
        try:
            visitor = Visitor.objects.get(name=name)
            return Response({'message': 'This name already exists'})
        except:
            serializer = VisitorSerializer(data=data)
            if serializer.is_valid():
                serializer_object = serializer.save()
                data = {
                'visitor': serializer.data,
                'id': serializer_object.id
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
                'registered_visitor': serializer.data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RepeatVisitorView(RetrieveUpdateAPIView):
    serializer_class = RegisterSerializer
    def patch(self,request,visitor_id):
        post_data = request.data
        temperature = post_data.get('temperature')
        visitor = Visitor.objects.get(pk=visitor_id)
        serialized_visitor = VisitorSerializer(visitor)
        repeat_visitor = Register.objects.get(visitor=visitor_id)
        repeat_visitor.temperature = temperature
        data = {
            'visitor': visitor_id,
            'temperature': temperature
        }
        serializer = RegisterSerializer(repeat_visitor, data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'registered_visitor': serializer.data,
                'visitor': serialized_visitor.data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
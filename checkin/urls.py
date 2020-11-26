from django.urls import path
from .views import  AddVisitor,RegisterVisitor

urlpatterns = [
    path('register/', RegisterVisitor.as_view()),
    path('add_visitor/', AddVisitor.as_view())
]
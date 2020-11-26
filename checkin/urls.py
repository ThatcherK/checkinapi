from django.urls import path
from .views import RegisterList, AddVisitor,RegisterVisitor,VisitorList

urlpatterns = [
    path('', RegisterList.as_view()),
    path('register/', RegisterVisitor.as_view()),
    path('add_visitor/', VisitorList.as_view())
]
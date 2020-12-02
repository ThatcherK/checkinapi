from django.urls import path
from .views import  AddVisitor,RegisterVisitor, RepeatVisitorView

urlpatterns = [
    path('register/', RegisterVisitor.as_view()),
    path('add_visitor/', AddVisitor.as_view()),
    path('repeat_visitor/<int:visitor_id>/', RepeatVisitorView.as_view() )
]
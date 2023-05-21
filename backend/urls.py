from django.urls import path 
from myapp.views import ProblemListView

urlpatterns = [
     path('problemlistview/', ProblemListView.as_view()),
]

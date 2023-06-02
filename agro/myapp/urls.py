from django.urls import path
from myapp import views
from myapp.views import ProblemListView, ProblemDetailView, ProblemCreateView
from django import forms

 
urlpatterns = [
   
    path('problemlistview/', ProblemListView.as_view()),
    path('problemlistview/problemcreateview/', ProblemCreateView.as_view()),
    path('problemlistview/problemcreateview/problemlistview', ProblemListView.as_view()),
    path('problemlistview/problemdetailview/<int:pk>', ProblemDetailView.as_view()),
    path('problemlistview/problemcreateview/problemdetailview/<int:pk>', ProblemDetailView.as_view()),
    path('problemcreateview/', ProblemCreateView.as_view()),
    
    path('feedbacklistview/', FeedbackListView.as_view()),
    path('feedbackcreateview/', FeedbackCreateView.as_view()),
    path('feedbacklistview/feedbackdetailview/<int:pk>', FeedbackDetailView.as_view()),
    path('feedbackdetailview/<int:pk>', FeedbackDetailView.as_view()),
    path('feedbacklistview/feedbackdetailview/', FeedbackDetailView.as_view()),
]

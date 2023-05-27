from django.urls import path
from myapp import views
from myapp.views import UserCreateView, UserListView, ProblemListView, ProblemDetailView, ProblemCreateView
from django import forms

 
urlpatterns = [
    path('usercreateview', UserCreateView.as_view()),
    path('userlistview', UserListView.as_view()),

    path('problemlistview/', ProblemListView.as_view()),
    path('problemdetailview/<int:pk>', ProblemDetailView.as_view()),
    path('problemcreateview', ProblemCreateView.as_view()),
]

from django.urls import path
from myapp import views
from myapp.views import UserCreateView, UserListView, ProblemListView, ProblemDetailView, ProblemCreateView
from myapp.views import FeedbackListView, FeedbackDetailView, FeedbackCreateView
from myapp.views import CategoryListView, CategoryCreateView
from django import forms

 
urlpatterns = [
    path('usercreateview', UserCreateView.as_view()),
    path('userlistview', UserListView.as_view()),

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

    path('categorylistview/', CategoryListView.as_view()),
    path('categorycreateview/', CategoryCreateView.as_view()),

    #path('category', views.category),
]

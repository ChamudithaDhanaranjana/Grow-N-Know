from django.urls import path,re_path
from myapp import views
from myapp.views import UserCreateView, UserListView, ProblemListView, ProblemDetailView, ProblemCreateView
from myapp.views import FeedbackListView, FeedbackDetailView, FeedbackCreateView
from myapp.views import CategoryListView, CategoryCreateView
from myapp.views import ItemListView, ItemCreateView
from myapp.views import OrderListView, OrderCreateView
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
    path('feedbacklistview/feedbackcreateview/', FeedbackCreateView.as_view()),
    path('feedbackdetailview/<int:pk>', FeedbackDetailView.as_view()),
    path('feedbackcreateview/feedbackdetailview/', FeedbackDetailView.as_view()),
    path('feedbacklistview/feedbackcreateview/feedbacklistview', FeedbackListView.as_view()),
    path('feedbacklistview/feedbackcreateview/feedbackdetailview/<int:pk>', FeedbackDetailView.as_view()),

    path('categorylistview/', CategoryListView.as_view()),
    path('categorycreateview/', CategoryCreateView.as_view()),

    path('itemlistview/', ItemListView.as_view()),
    path('itemcreateview/', ItemCreateView.as_view()),

    path('orderlistview/', OrderListView.as_view()),
    path('ordercreateview/', OrderCreateView.as_view()),

    re_path(r'^items/(?P<pk>\d+)?$',views.item),
    re_path(r'^orders/(?P<pk>\d+)?$',views.order),
]

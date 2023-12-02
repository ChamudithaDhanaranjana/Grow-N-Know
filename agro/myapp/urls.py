from django.urls import path, re_path
from myapp.views import SolutionRemoveView, SolutionUpdateView
from myapp.views import SolutionListView
from myapp import views
from myapp.views import ProblemListView, ProblemDetailView, ProblemCreateView
from myapp.views import FeedbackListView, FeedbackDetailView, FeedbackCreateView
from myapp.views import CategoryListView, CategoryCreateView
from myapp.views import ItemListView, ItemCreateView
from myapp.views import OrderListView, OrderCreateView
 # Import the cart views

urlpatterns = [

    path('problemlistview/', ProblemListView.as_view()),
    path('problemlistview/problemcreateview/', ProblemCreateView.as_view(), name='problem_create'),
    path('problemlistview/problemcreateview/problemlistview', ProblemListView.as_view()),
    path('problemlistview/problemdetailview/<int:pk>', ProblemDetailView.as_view()),
    path('problemlistview/problemcreateview/problemdetailview/<int:pk>', ProblemDetailView.as_view()),
    path('problemcreateview/', ProblemCreateView.as_view(), name='problem_create'),
    
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

    re_path(r'^items/(?P<pk>\d+)?$', views.item),
    re_path(r'^orders/(?P<pk>\d+)?$', views.order),

    path('problem/<int:problem_id>/solution_create/', views.add_solution),
    path('problem/<int:problem_id>/add_solution/', views.add_solution, name='add_solution'),
    path('problem/<int:pk>/', views.ProblemDetailView.as_view(), name='problem_detail'),
    path('problem/<int:pk>/', views.problem_detail),
    path('problem/<int:pk>/solutions/', views.SolutionListView.as_view(), name='solution_list'),
    path('problem/<int:problem_id>/solutions/', SolutionListView.as_view(), name='problem_solutions'),
    path('solution/remove/<int:pk>/', SolutionRemoveView.as_view(), name='solution_remove'),
    path('solution/update/<int:pk>/', SolutionUpdateView.as_view(), name='solution_update'),
    path('solution/remove/<int:pk>/', SolutionRemoveView.as_view(), name='solution_remove'),


    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ma_vue, name='ma_page'),
    path('details/<str:category_name>/', views.details_view, name='details_page'),
    path('api/add-order/', views.add_order_to_firebase, name='add_order_to_firebase'),
   
]
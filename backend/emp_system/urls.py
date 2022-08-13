from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('view_emp',views.view_emp,name = 'view_emp'),
    path('add_emp',views.add_emp,name = 'add_emp'),
    path('delete_emp',views.delete_emp,name = 'delete_emp'),
    path('filter_emp',views.filter_emp,name = 'filter_emp'),
]
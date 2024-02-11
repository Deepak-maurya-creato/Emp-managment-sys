from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-employee/', views.all_emp, name="all-employee"),
    path('add-employee/', views.add_emp, name="add-employee"),
    path('delete-employee/', views.delete_emp, name="delete-employee"),
     path('delete-employee/<int:emp_id>/', views.delete_emp, name="delete-employee"),
    path('filter-employee/', views.filter_emp, name="filter-employee"),
]



from django.urls import path
from . import views

urlpatterns = [
    path('add_employee/', views.add_employee, name='add_employee'), 
    path('edit_employee/', views.home, name='edit_employee'), 
    path('update_employee/<int:id>/', views.update_employee, name='update_employee'), 
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'), 
    path('view_profile/<int:id>/', views.view_profile, name='view_profile'), 
]








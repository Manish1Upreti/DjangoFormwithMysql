from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='employee_show'),
    path('emp/', views.emp, name='employee_list'),
    path('edit/<int:id>', views.edit, name='employee_edit'),
    path('update/<int:id>', views.update, name='employee_update'),
    path('delete/<int:id>', views.destroy, name='employee_delete'),
]
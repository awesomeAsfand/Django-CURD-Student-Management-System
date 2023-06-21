from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('details/<int:student_id>/', views.details, name='details'),
    path('delete/<int:student_id>/', views.delete, name='delete'),
    path('update/<int:student_id>/', views.update, name='update'),
    path('add_marks/<int:student_id>/', views.add_marks, name='add_marks'),
]


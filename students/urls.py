from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
]
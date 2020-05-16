from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('login/submit_login,', views.login),
        path('login/password_change/', views.change_password),
        path('logout/', views.logout),
        path('edit/', views.change_user),
        path('login/', views.login),
        path('edit_table/', views.create_table), 
        path('<str:userName>/', views.display_user),
        path('login/submit/', views.model_form_submit),
]

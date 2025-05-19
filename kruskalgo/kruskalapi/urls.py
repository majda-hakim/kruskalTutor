from django.urls import path , include
from . import views 

urlpatterns = [
    path('register/', views.Register,name="register"),
    path('login/', views.Login,name="login"),
    path('users/', views.get_user_list, name='user_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
]
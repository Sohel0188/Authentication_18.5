
from django.urls import path
from . import views
urlpatterns = [
  
    path('register/', views.signup, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('changePassword/', views.changePassword, name="changePassword"),
]

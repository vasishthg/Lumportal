from django.urls import path

from . import views
app_name = "users"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('oomplogin/', views.oomplogin, name="oomplogin"),
    path('logout/', views.logout, name="logout")
]

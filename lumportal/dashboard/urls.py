from django.urls import path

from . import views
app_name = "dashboard"
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('oompa/', views.oompa, name='oompadashboard'),
    path('shop/', views.shop, name='shop'),
    path('shop/buy/', views.buy, name="buy"),
    path('training/', views.training, name="training"),
    path('trainingpost/', views.trainingpost, name="trainingpost"),
    path('shop/buy/oompa/', views.buyoompa, name="buyoompa")
]

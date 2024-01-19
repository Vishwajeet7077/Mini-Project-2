from django.urls import path, include
from . import views
urlpatterns = [ 
    path('', views.home, name="home"), 
    path('get_rate/<str:company_name>/', views.get_rate, name='get_rate')

]

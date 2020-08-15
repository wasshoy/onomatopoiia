from django.urls import path

from . import views


app_name = 'onomato'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tos/', views.tos, name='tos'),
    path('contact/', views.contact, name='contact'),
    path('odai/', views.odai_index, name='odai_index'),
    path('odai/<int:odai_id>/', views.odai_detail, name='odai_detail'),
]

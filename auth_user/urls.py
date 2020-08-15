import django.contrib.auth.views
from django.urls import path,include
from . import views
app_name='auth_user'

urlpatterns=[
    path('top/',views.top_page, name="top"), # リダイレクト
    path('login/', # ログイン
         django.contrib.auth.views.LoginView.as_view(),
         {
             'template_name': 'auth_user/login.html',
         },
         name='login'),
    path('logout/', # ログアウト
         django.contrib.auth.views.LogoutView.as_view(),
         {
             'template_name': 'auth_user/logout.html',
         },
         name='logout'),
]
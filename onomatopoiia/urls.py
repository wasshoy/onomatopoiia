from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', )
    path('onomato/', include('onomato.urls')),
    path('user/', include('auth_user.urls')),
    path('user/', include('social_django.urls', namespace='social')),
]

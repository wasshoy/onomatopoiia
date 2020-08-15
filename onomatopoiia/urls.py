from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('onomato.urls')),  # TODO: onomato/ を / にして動くようにする
    # path('onomato/', include('onomato.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # 標準ユーザー機能のために追加
    path('accounts/', include('accounts.urls')),
]

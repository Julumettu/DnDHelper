from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from creatures import views as creatures_views
from items import views as items_views
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/monsters/', creatures_views.monsterList.as_view()),
    path('api/items/', items_views.itemsList.as_view()),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


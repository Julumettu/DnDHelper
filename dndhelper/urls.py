from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from creatures import views
from django.conf.urls import url

urlpatterns = [
    path('creatures/', include('creatures.urls')),
    path('api/monsters/', views.monsterList.as_view()),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


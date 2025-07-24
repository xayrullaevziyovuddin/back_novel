from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Импортируем ViewSets
from novel.views import VolumeViewSet, ChapterViewSet
from wiki.views import CharacterViewSet
from anime.views import AnimeSeasonViewSet, EpisodeViewSet

# Настройка Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Reincarnated Unemployed API",
      default_version='v1',
      description="API для сайта о ранобэ и аниме 'Ренкорнация безработного'",
      contact=openapi.Contact(email="admin@example.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Роутер для API
router = DefaultRouter()
router.register(r'volumes', VolumeViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'anime-seasons', AnimeSeasonViewSet)
router.register(r'episodes', EpisodeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Для отображения медиа файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
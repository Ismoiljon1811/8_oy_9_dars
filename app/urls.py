from django.urls import path, include

from .views import BlogView, BlogViewAll, CommentView, CommentViewAll, LIkeView, LIkeViewAll

from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = routers.SimpleRouter()
router.register('blog_all', BlogViewAll)
router.register('comment_all', CommentViewAll)
router.register('like_all', LIkeViewAll)
router.register('blog', BlogView)
router.register('comment', CommentView)
router.register('like', LIkeView)

urlpatterns = [
    path('ap/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    
]
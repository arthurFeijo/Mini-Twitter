from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
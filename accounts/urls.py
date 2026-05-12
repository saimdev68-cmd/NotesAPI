from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    UserViewSet,
    ProfileViewSet,
    StaffUserView,
    AdminUserViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = DefaultRouter()
router.register("auth",UserViewSet,basename="auth")
router.register("admin",AdminUserViewSet)
router.register("staff",StaffUserView,basename="staff")
router.register("profile",ProfileViewSet,basename="profile")

urlpatterns = router.urls + [
    path("token/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view())
]
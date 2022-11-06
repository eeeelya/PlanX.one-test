from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from user.views import UserInfoViewSet, LoginView

router = DefaultRouter()
router.register("", UserInfoViewSet, basename="user-info")

urlpatterns = [
    path("user/", include(router.urls)),

    path("register/", UserViewSet.as_view({"post": "create"}), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
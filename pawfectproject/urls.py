from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from pawfectapi.views import *
from pawfectapi.views.register import login_user, register_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"pets", Pets, "pet")
router.register(r"playstyles", PlayStyles, "playstyle")
router.register(r"sizes", Sizes, "sizes")
router.register(r"users", Users, "user")
# router.register(r"favorites", Favorites, "favorites")

urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("api-token-auth", obtain_auth_token),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from pawfectapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"pets", Pets, "pet")
router.register(r"playstyles", PlayStyles, "playstyle")
router.register(r"sizes", Sizes, "sizes")
# router.register(r"favorites", Favorites, "favorites")

urlpatterns = [
    path("", include(router.urls)),
]

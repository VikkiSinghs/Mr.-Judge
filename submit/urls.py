from django.contrib import admin
from django.urls import path, include
from submit.views import submit

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("auth/", include("accounts.urls")),
    # path("home/", include("home.urls")),
    path("", submit, name="submit"),
]
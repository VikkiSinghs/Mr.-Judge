from django.urls import path
from home.views import all_qus,qu_detail

urlpatterns = [
    path("qus/", all_qus, name="all-qus"),
    path("qus/<int:qu_id>/", qu_detail, name="qu-detail"),
] 
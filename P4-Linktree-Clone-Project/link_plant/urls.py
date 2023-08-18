from django.urls import path
from .views import LinkListView, LinkCreateView, LinkUpdateView

urlpatterns = [
    path("", LinkListView.as_view(), name="link-list"),
    path("link/create/", LinkCreateView.as_view(), name="link-create"),
    path("link/<int:pk>/update/", LinkUpdateView.as_view(), name="link-update"),
]

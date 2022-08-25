from django.urls import path
from .views import SnackListView, SnackCreateView, SnackDeleteView, SnackDetailView, SnackUpdateView

urlpatterns = [
    path("list/", SnackListView(), name="snack_list"),
    path("detail/<int:pk>/", SnackDetailView(), name="snacK_detail"),
    path("create/", SnackCreateView.as_view(), name="snack_create.html"),
    path("update/<int:pk>/", SnackUpdateView(), name="snack_update"),
    path("delete/<int:pk>", SnackDeleteView(), name="snack_delete"),
]
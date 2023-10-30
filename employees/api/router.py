from django.urls import path

from employees.api.views import ListManagersView, ListSubordinatesView

urlpatterns = [
    path('managers/', ListManagersView.as_view(), name='list-managers'),
    path('managers/<int:manager_id>/subordinates/', ListSubordinatesView.as_view(), name='list-subordinates'),
]

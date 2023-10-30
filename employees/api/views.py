from rest_framework import generics
from employees.api.serializers import ManagerSerializer, SubordinateSerializer
from employees.models import Employee


def _is_manager(employee):
    """
    Determina si un empleado es un manager basándose en el campo organizationnode.
    """
    subordinates = Employee.objects.filter(
        organizationnode__startswith=employee.organizationnode
    ).exclude(businessentityid=employee.businessentityid)
    return subordinates.exists()


def _get_subordinates(manager):
    """
    Obtiene los subordinados de un manager basándose en el campo organizationnode.
    """
    return Employee.objects.filter(
        organizationnode__startswith=manager.organizationnode
    ).exclude(businessentityid=manager.businessentityid)


class ListManagersView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = ManagerSerializer

    def get_queryset(self):
        return [employee for employee in self.queryset.all() if _is_manager(employee)]


class ListSubordinatesView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = SubordinateSerializer

    def get_queryset(self):
        manager_id = self.kwargs["manager_id"]
        manager = Employee.objects.get(businessentityid=manager_id)
        return _get_subordinates(manager)

from rest_framework import serializers
from employees.models import Employee


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["businessentityid", "loginid", "jobtitle"]


class SubordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["businessentityid", "loginid", "jobtitle"]

from rest_framework import serializers

from snippet.models import Asset, Department, Project


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["name"]


class DepartmentSerializer(serializers.ModelSerializer):
    assets = AssetSerializer(source="asset", many = True)

    class Meta:
        model = Department
        fields = ["name", "assets"]


class ProjectSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(source="department", many=True)

    class Meta:
        model = Project
        fields = ["name", "departments"]

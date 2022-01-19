from django.db import models


class Asset(models.Model):
    class Meta:
        db_table = "asset"

    name = models.CharField(max_length=255)


class Department(models.Model):
    class Meta:
        db_table = "department"

    name = models.CharField(max_length=255)
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, related_name="asset_department"
    )


class Project(models.Model):
    class Meta:
        db_table = "project"

    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="asset_department"
    )

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from snippet.models import Project
from snippet.serializers import ProjectSerializer


class SearchView(viewsets.ViewSet):
    @staticmethod
    def create(request):
        search = request.data.get("search")
        query = Q()
        if search:
            query.add(
                Q(name__icontains=search)
                | Q(department__name__icontains=search)
                | Q(department__asset__name__icontains=search),
                query.connector,
            )
        return Response(
            ProjectSerializer(Project.objects.filter(query), many=True).data
        )

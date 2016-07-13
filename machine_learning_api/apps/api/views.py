from django.http.response import HttpResponseForbidden, HttpResponseNotFound

from rest_framework import viewsets

from serializers import CatSerializer, CatComputedSerializer
from models import CatModel


class CatViewSet(viewsets.ModelViewSet):
    queryset = CatModel.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        serializers = {
            'retrieve': CatComputedSerializer,
        }
        print(self.action)
        return serializers.get(self.action, CatSerializer)

    def retrieve(self, request, *args, **kwargs):
        return HttpResponseNotFound("Retrieve one")

    def list(self, request, *args, **kwargs):
        return HttpResponseForbidden("Not allowed to list!")

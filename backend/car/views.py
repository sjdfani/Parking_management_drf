from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import CarSerializer
from .models import Car
from .permission import IsStaff, IsSuperUser


class CarManagement(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        if self.action not in ['list', 'retrieve']:
            permission_classes = [IsSuperUser, IsStaff]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

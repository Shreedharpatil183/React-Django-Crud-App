import imp
from rest_framework import viewsets
from .models import *
from .serializers import *


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from rest_framework import viewsets
from .models import *
from .serializers import *


class SectionViewSets(viewsets.ModelViewSet):

    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class StaffViewSets(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from pollen_counts.quickstart.serializers import UserSerializer, GroupSerializer, PollenCountSerializer
from pollen_counts.quickstart.models import PollenCounts


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PollenCountsViewSet(viewsets.ModelViewSet):
    queryset = PollenCounts.objects.all().order_by('-date')
    serializer_class = PollenCountSerializer

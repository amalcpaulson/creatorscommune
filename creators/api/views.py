from .models import Event, Member
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer, MemberSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
from rest_framework import serializers
from .models import Event, Member

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["name", "date", "time", "description", "link", "photo"]
        

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["name", "designation", "description", "photo"]
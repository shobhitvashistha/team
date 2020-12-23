from rest_framework import serializers
from members.models import TeamMember


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'role')
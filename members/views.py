# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from members.models import TeamMember
from members.serializers import TeamSerializer


@api_view(['GET', 'POST'])
def team(request):
    if request.method == 'GET':
        team_members = TeamMember.objects.all()
        serializer = TeamSerializer(team_members, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def team_member(request, pk):
    try:
        member = TeamMember.objects.get(pk=pk)
    except TeamMember.DoesNotExist:
        return Response({'details': 'TeamMember with id=%s does not exist' % pk}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializer(member)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = TeamSerializer(member, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


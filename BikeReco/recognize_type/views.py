from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
#from rest_framework.response import Response
from django.http import HttpResponse
from recognize_type.models import Recognizer
from recognize_type.serializers import RecognizeSerializer
from recognize_type.serializers import UserSerializer, GroupSerializer, RecognizeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class recognizeView(APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = RecognizeSerializer

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        #TODO return proper response
        todos = Recognizer.objects.filter(user = request.user.id)
        serializer = RecognizeSerializer(todos, many=True)
        return HttpResponse("1", status=status.HTTP_200_OK)
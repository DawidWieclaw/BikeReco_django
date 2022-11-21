from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
#from rest_framework.response import Response
from django.http import HttpResponse
from recognize_type.models import Recognizer, NNModel
from recognize_type.serializers import RecognizeSerializer
from recognize_type.serializers import UserSerializer, GroupSerializer, RecognizeSerializer

from PIL import Image
from io import BytesIO
import base64

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
        return HttpResponse("gitara", status=status.HTTP_200_OK)

    # 1. List all
    def post(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        img = Image.open(BytesIO(base64.b64decode(request.POST['image'])))
        print(type(img))
        model = NNModel()
        pred = model.predict(img)
        print("PRED: " + str(pred) + "\n")
        #TODO return proper response

        #todos = Recognizer.objects.filter(user = request.user.id)
        #serializer = RecognizeSerializer(todos, many=True)
        if pred == 0:
            return HttpResponse("MTB", status=status.HTTP_200_OK)
        elif pred == 1:
            return HttpResponse("ROAD", status=status.HTTP_200_OK)
        elif pred == 2:
            return HttpResponse("CITY", status=status.HTTP_200_OK)
        else:
            return HttpResponse("ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
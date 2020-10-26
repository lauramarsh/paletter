from django.http import request
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import views
from rest_framework import status
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from be_paletter.models import Palettes
from be_paletter.serializers import PalettesSerializer, UserSerializer, GroupSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET', 'POST'])
def palettes_list(request, format=None):

    if request.method == 'GET':
        palettes = Palettes.objects.all()
        serializer = PalettesSerializer(palettes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PalettesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def palettes_detail(request, pk, format=None):
    try:
        palette = Palettes.objects.get(pk=pk)
    except Palettes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PalettesSerializer(palette)
        return Response(serializer.data)
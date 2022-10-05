from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404

from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .serializers import InstructorSerializer, TrainerSerializer, GallerySerializer,MyTokenObtainPairSerializer, RegisterSerializer
from .models import Instructor, Trainer, Gallery

from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


#Instructor
@api_view(['GET'])
def getInstructors(request):
    datas = Instructor.objects.all()
    serializer = InstructorSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getInstructor(request, pk):
    data = Instructor.objects.get(id=pk)
    serializer = InstructorSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postInstructor(request):
    reqData = request.data
    serializer = InstructorSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def putInstructor(request, pk):
    reqData = request.data
    data = Instructor.objects.get(id=pk)
    serializer = InstructorSerializer(instance=data, data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteInstructor(request, pk):
    data = Instructor.objects.get(id=pk)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#Trainer
@api_view(['GET'])
def getTrainers(request):
    datas = Trainer.objects.all()
    serializer = TrainerSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTrainer(request, pk):
    data = Trainer.objects.get(id=pk)
    serializer = TrainerSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postTrainer(request):
    reqData = request.data
    serializer = TrainerSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def putTrainer(request, pk):
    reqData = request.data
    data = Trainer.objects.get(id=pk)
    serializer = TrainerSerializer(instance=data, data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteTrainer(request, pk):
    data = Trainer.objects.get(id=pk)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#Gallery
@api_view(['GET'])
def getGallerys(request):
    datas = Gallery.objects.all()
    serializer = GallerySerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGallery(request, pk):
    data = Gallery.objects.get(id=pk)
    serializer = GallerySerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postGallery(request):
    reqData = request.data
    serializer = GallerySerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def putGallery(request, pk):
    reqData = request.data
    data = Gallery.objects.get(id=pk)
    serializer = GallerySerializer(instance=data, data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteGallery(request, pk):
    data = Gallery.objects.get(id=pk)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
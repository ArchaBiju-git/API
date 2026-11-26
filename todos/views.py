
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Todo
from.serializers import RegisterSerializer,TodoSerializer
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class=TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class LogoutView(APIView):
    def post(self,request):
        refresh_token= request.data.get('refresh')

        if not refresh_token:
            return Response({'error':'Refresh token is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token= RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response({'error':'Invalid refresh token'},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {'message':'Logout successfull'},
            status=status.HTTP_200_OK
        )
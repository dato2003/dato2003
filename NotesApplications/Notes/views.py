from rest_framework import generics,status
from .serializer import UserSerializer , NoteSerializer,userloginserialzer
from rest_framework.views import APIView
from django.contrib.auth import login,logout,authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notes



class RegisterView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request):
        serializer = userloginserialzer(data=request.data)
        if  not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(username = username,password = password)
    

        if user  is None:
            return Response({"error":"wrong password or username"},status=status.HTTP_400_BAD_REQUEST)
        login(request,user)
        return Response(UserSerializer(user).data)
       

class LogoutView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        logout(request)

        return Response (status=status.HTTP_200_OK)
    
class NoteView(generics.ListCreateAPIView):
    queryset= Notes.objects.all()
    serializer_class = NoteSerializer

class NoteDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
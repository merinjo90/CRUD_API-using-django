
from django.shortcuts import render
from .serializers import UserRegister,ArticleInfSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ArticleInf
from rest_framework import status

# Create your views here.

class Register(APIView):
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)

class Welcome(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)

class ArticleinfoTable(APIView):
    def get(self,request):
        artobj=ArticleInf.objects.all()
        artserializeobj=ArticleInfSerializer(artobj,many=True)
        return Response(artserializeobj.data)

    def post(self,request):
        serializeobj=ArticleInfSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleUpdatedel(APIView):
    def get_object(self, pk):
        try:
            return ArticleInf.objects.get(pk=pk)
        except ArticleInf.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        artobj=self.get_object(pk)
        seralizeobj=ArticleInfSerializer(artobj)
        return Response(seralizeobj.data)

    def put(self,request,pk):
        artobj=self.get_object(pk)
        artserialize=ArticleInfSerializer(artobj,data=request.data)
        if artserialize.is_valid():
            artserialize.save()
            return Response(artserialize.data,status=status.HTTP_200_OK)
        return Response(artserialize.errors,status=status.HTTP_400_BAD_REQUEST)



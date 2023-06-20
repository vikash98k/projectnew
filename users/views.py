from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
import json
class PersonRegisterPostView(APIView):
    def post(self,request):
        request_data = request.data
        serializer = PersonSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class PersonRegisterGetView(APIView):
    def post(self,request):
        person = Person.objects.all()
        serializer = PersonSerializer(person,many=True)
        return Response(serializer.data)
    

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        person = Person.objects.all()
        return person
    
class ProfileRegisterView(APIView):

    def post(self,request):
        pass


class PersonDataInputView(APIView):
    def post(self,request):
        data = open(r'C:\Users\V\Desktop\response.json')
        sol = json.load(data)
        for i in sol:
            person=Person.objects.create(first_name=i["first_name"],last_name=i["last_name"],roll_no=i["roll_no"],gender=i["gender"])
            person.save()
        return Response(sol)
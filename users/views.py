from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

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
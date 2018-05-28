from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MiSerializer
from rest_framework import  serializers
import datetime

class MiVistaSet(viewsets.ViewSet):
    
    ##LE PASO LOS DATOS QUE RECIBE "MiSerializer" y lo devuelvo como json
    def list(self, request):
        hora=datetime.datetime.now().isoformat()
        yourdata= [{"id": 1, "hora_actual": hora}]
        serializer = MiSerializer(yourdata, many=True)
        return Response(serializer.data)

# Create your views here.

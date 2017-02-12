from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

class StockList(APIView):

    def get(self,request):
        stock = Stock.objects.all()
        serialize = StockSerializer(stock,many = True)
        return Response(serialize.data)

    def post(self):
        pass
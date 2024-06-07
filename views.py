from django.http import JsonResponse
from django.shortcuts import render
from .models import Drink
from .serializers import DrinksSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template.response import TemplateResponse

@api_view(['GET','POST'])
def drink_list (request):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinksSerializers(drinks, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DrinksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail (request, id):
    try:
        drink = Drink.objects.get(pk=id)
    except:
        Drink.DoesNotExist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinksSerializers(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinksSerializers(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def home(request):
    Drinks =  Drink.objects.all()
    context = { 'drinks': Drinks}
    return render(request, "index.html", context)

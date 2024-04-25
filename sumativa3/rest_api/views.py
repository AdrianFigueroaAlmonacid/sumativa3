from django.shortcuts import render
from core.models import series
from .serializers import seriesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_series(request):
    if request.method == 'GET':
        serie = series.objects.all()
        serializer = seriesSerializer(serie, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = seriesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def vista_serie(request, id):
    try:
        serie = series.objects.get(id=id)
    except serie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = seriesSerializer(serie)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = seriesSerializer(serie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

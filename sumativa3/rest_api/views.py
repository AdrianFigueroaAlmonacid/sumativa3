from django.shortcuts import render
from core.models import series
from .serializers import seriesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_series(request):
    if request.method == 'GET':
        serie = series.objects.all()
        serializer = seriesSerializer(serie, many=True)

        return Response(serializer.data)

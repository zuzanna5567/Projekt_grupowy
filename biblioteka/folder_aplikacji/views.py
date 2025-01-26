from datetime import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Autor, Czytelnik, Kategoria, Ksiazka, Wypozyczenie
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import AutorSerializer, CzytelnikSerializer, KategoriaSerializer, KsiazkaSerializer, WypozyczenieSerializer

@api_view(['GET', 'POST'])
def kategoria_list(request):
    if request.method == 'GET':
        kategorie = Kategoria.objects.all()  # Pobieramy wszystkie kategorie
        serializer = KategoriaSerializer(kategorie, many=True)  # Serializujemy dane
        return Response(serializer.data)  # Zwracamy dane w odpowiedzi

    elif request.method == 'POST':
        serializer = KategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Zapisujemy nową kategorię
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Zwracamy dane i status 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # W przypadku błędu walidacji

@api_view(['GET', 'POST'])
def autor_list(request):
    if request.method == 'GET':
        autorzy = Autor.objects.all()  # Pobieramy wszystkich autorów
        serializer = AutorSerializer(autorzy, many=True)  # Serializujemy dane
        return Response(serializer.data)  # Zwracamy dane w odpowiedzi

    elif request.method == 'POST':
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Zapisujemy nowego autora
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Zwracamy dane i status 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # W przypadku błędu walidacji

@api_view(['GET', 'PUT', 'DELETE'])
def kategoria_details(request, pk):
    try:
        kategoria = Kategoria.objects.get(pk=pk)
    except Kategoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = KategoriaSerializer(kategoria)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = KategoriaSerializer(kategoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kategoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def autor_details(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def ksiazka_list(request):
    if request.method == 'GET':
        ksiazki = Ksiazka.objects.all()
        serializer = KsiazkaSerializer(ksiazki, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KsiazkaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ksiazka_details(request, pk):
    try:
        ksiazka = Ksiazka.objects.get(pk=pk)
    except Ksiazka.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = KsiazkaSerializer(ksiazka)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = KsiazkaSerializer(ksiazka, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ksiazka.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def czytelnik_list(request):
    if request.method == 'GET':
        czytelnicy = Czytelnik.objects.all()
        serializer = CzytelnikSerializer(czytelnicy, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CzytelnikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def czytelnik_details(request, pk):
    try:
        czytelnik = Czytelnik.objects.get(pk=pk)
    except Czytelnik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CzytelnikSerializer(czytelnik)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CzytelnikSerializer(czytelnik, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        czytelnik.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def wypozyczenie_list(request):
    if request.method == 'GET':
        wypozyczenia = Wypozyczenie.objects.all()
        serializer = WypozyczenieSerializer(wypozyczenia, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WypozyczenieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def wypozyczenie_details(request, pk):
    try:
        wypozyczenie = Wypozyczenie.objects.get(pk=pk)
    except Wypozyczenie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WypozyczenieSerializer(wypozyczenie)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = WypozyczenieSerializer(wypozyczenie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wypozyczenie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Widok powitalny
def welcome_view(request):
    now = datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)
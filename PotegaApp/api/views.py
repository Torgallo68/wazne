from django.db import router
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

# Create your views here.


def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateView(request, pk):
    try:
        note = Note.objects.get(id=pk)  # Pobieranie notatki o podanym ID
    except Note.DoesNotExist:
        return Response({"error": "Note not found"}, status=404)  # Obsługa błędu 404 jeśli notatka nie istnieje

    data = request.data
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()  # Zapisujemy zaktualizowaną notatkę

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    try:
        note = Note.objects.get(id=pk)  # Pobieranie notatki o podanym ID
        note.delete()  # Usuwanie notatki
        return Response(status=204)  # Zwrócenie statusu 204 bez zawartości
    except Note.DoesNotExist:
        return Response({"error": "Note not found"}, status=404)
    
@api_view(['POST'])
def createView(request):
    data = request.data
    note = Note.objects.create(
        name=data.get('name', ''),
        weight=data.get('weight', ''),
        sets=data.get('sets', ''),
        reps=data.get('reps', ''),
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


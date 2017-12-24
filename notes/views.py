from django.shortcuts import render
from notes.models import Note


def index_view(request):
	notes = Note.objects.all()
	return render(request, 'notes/index.html', {'notes' : notes})

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from notes.models import Note
from notes.forms import NoteForm


def index_view(request):
    notes = Note.objects.all().filter(owner=request.user)
    return render(request, 'notes/index.html', {'notes' : notes})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = NoteForm()

    return render(request, 'notes/addnote.html', {'form': form})

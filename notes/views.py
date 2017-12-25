from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from notes.models import Note
from notes.forms import NoteForm


def index_view(request):
    notes = Note.objects.all().filter(owner=request.user)
    notes = notes.order_by('-timestamp')
    return render(request, 'notes/index.html', {'notes' : notes})


def add_note(request):
    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Note, id=id)
    else:
        note = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, 'Note Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))

        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form': form})

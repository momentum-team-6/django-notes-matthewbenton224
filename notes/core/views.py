from django.shortcuts import render, redirect, get_object_or_404
from core.data import NOTES
from core.models import Note
from .forms import NoteForm, SearchForm

# Create your views here.
def list_notes(request):
    notes = Note.objects.all()
    form = SearchForm() 
    return render(request, 'core/home.html', {"notes": notes, 'form': form})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "core/note_detail.html", {'note': note})

def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='notes_list')

    return render(request, 'core/add_note.html', {'form': form})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect(to='notes_list')

    return render(request, 'core/delete_note.html', {'note': note})

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(to='notes_list')
    return render(request, "core/edit_note.html", {
        "form": form,
        "note": note
    })

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            notes = Note.objects.filter(body__icontains=search)
            return render(request, "core/search.html", 
                {"notes": notes})
    else:
        return render(request, "core/search.html")



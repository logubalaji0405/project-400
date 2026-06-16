from django.shortcuts import render, redirect

from .models import Editor
from .forms import EditorForm, ContactForm

# Optional
# from .instagram_tracker import get_followers


def home(request):

    editors = Editor.objects.all()

    return render(request, 'home.html', {
        'editors': editors
    })


def add_editor(request):

    if request.method == 'POST':

        form = EditorForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('add_editor')

    else:
        form = EditorForm()

    return render(request, 'add_editor.html', {
        'form': form
    })


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })


def instagram_live(request):

    # Temporary static data
    data = [
        {
            'username': 'virat.kohli',
            'followers': '270M'
        },
        {
            'username': 'leomessi',
            'followers': '505M'
        }
    ]

    return render(request, 'instagram_live.html', {
        'data': data
    })
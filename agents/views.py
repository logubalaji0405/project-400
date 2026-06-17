from django.shortcuts import render, redirect

from .models import Editor, Like, Comment
from .forms import EditorForm, ContactForm
from django.shortcuts import render, get_object_or_404

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




def projects(request):
    editors = Editor.objects.all()

    return render(request, 'projects.html', {
        'editors': editors
    })


from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

@login_required
def add_like(request, pk):

    if request.method == "POST":

        editor = Editor.objects.get(id=pk)

        Like.objects.create(editor=editor)

        return JsonResponse({
            "success": True,
            "likes": editor.like_set.count()
        })

    return JsonResponse({
        "success": False
    })


def add_comment(request, pk):

    editor = Editor.objects.get(id=pk)

    Comment.objects.create(
        editor=editor,
        name=request.POST.get('name'),
        comment=request.POST.get('comment')
    )

    comments = ""

    for comment in editor.comment_set.all().order_by('-id'):

        comments += f"""
        <div class='mb-3'>
            <strong>{comment.name}</strong><br>
            {comment.comment}
        </div>
        """

    return JsonResponse({
        'comments': comments
    })
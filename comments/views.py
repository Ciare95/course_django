from django.shortcuts import render
from django.http import HttpResponse

from comments.forms import CommentForm
from comments.models import Comment

def home_page_view(request):
    content = 'Hello world'
    return HttpResponse(content)

def add(request):

    if request.method == 'GET':
        form = CommentForm()
        return render(
            request,
            'comments/add.html',
            {'form': form}
        )

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'comments/add.html',
                {'form': form}
            )
        


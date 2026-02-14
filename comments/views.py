from django.shortcuts import render, redirect
from comments.models import Comment

from comments.forms import CommentForm


def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments_list')
    else:
        form = CommentForm()

    return render(request, 'comments/add.html', {'form': form})

def show_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        return render(
            request,
            'comments/comments_list.html',
            {'comments_list': comments}
        )






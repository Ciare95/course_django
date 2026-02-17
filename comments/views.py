from django.shortcuts import render, redirect, get_object_or_404
from comments.models import Comment

from comments.forms import CommentForm


def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments:comments_list')
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

def get_only_comment(request, id):

    if request.method == 'GET':
        get_comment = Comment.objects.get(id=id)
        return render(
            request,
            'comments/comment_detail.html',
            {'comment_detail': get_comment}
        )

def update_comment(request, id):

    comment = get_object_or_404(Comment, id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comments:comments_list')
    else:
        form = CommentForm(instance=comment)
        return render(
            request,
            'comments/update_comment.html',
            {'form_update': form}
        )

def delete_comment(request, id):

    comment = Comment.objects.filter(id=id)
    comment.delete()

    return redirect('comments:comments_list')







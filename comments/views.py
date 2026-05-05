from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from comments.models import Comment

from comments.forms import CommentForm

COMMENTS_LIST_ROUTE = 'comments:comments_list'


def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(COMMENTS_LIST_ROUTE)
    else:
        form = CommentForm()

    return render(request, 'comments/add.html', {'form': form})

def show_list(request):

    comment_list = Comment.objects.all()
    paginator = Paginator(comment_list, 2)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)

    if request.method == 'GET':
        return render(
            request,
            'comments/comments_list.html',
            {'comments_list': comments_page}
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
            return redirect(COMMENTS_LIST_ROUTE)
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

    return redirect(COMMENTS_LIST_ROUTE)







from django.urls import path
from comments.views import add, show_list

app_name = 'comments'

urlpatterns = [
    path('add', add, name='add'),
    path('comments_list', show_list, name='comments_list'),
]
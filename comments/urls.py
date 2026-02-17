from django.urls import path
from comments.views import add, show_list, get_only_comment, update_comment, delete_comment

app_name = 'comments'

urlpatterns = [
    path('add', add, name='add'),
    path('comments_list', show_list, name='comments_list'),
    path('get_comment/<int:id>/', get_only_comment, name='get_only_comment'),
    path('update_comment/<int:id>/', update_comment, name='update_comment'),
    path('delete_comment/<int:id>/', delete_comment, name='delete_comment'),
]
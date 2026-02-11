from django.urls import path
from comments.views import add

app_name = 'comments'

urlpatterns = [
    path('add', add, name='add'),
]
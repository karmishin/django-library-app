from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('author/<int:pk>', views.AuthorView.as_view(), name='author_detail'),
]
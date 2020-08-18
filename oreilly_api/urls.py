from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.AllBookView.as_view(), name='book'),
    path("book/<int:id>", views.BookView.as_view(), name='a_book')
]
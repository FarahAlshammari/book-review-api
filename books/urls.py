from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    ReviewCreateView,
    BookReviewsView,
    ReviewUpdateView,
    ReviewDeleteView,
    RegisterView,
    ChangePasswordView,
)

urlpatterns = [
    # 📚 Books
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/create/', BookCreateView.as_view()),
    path('books/<int:pk>/update/', BookUpdateView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteView.as_view()),

    # 📝 Reviews
    path('reviews/add/', ReviewCreateView.as_view()),
    path('books/<int:book_id>/reviews/', BookReviewsView.as_view()),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view()),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view()),

    # 👤 Auth
    path('register/', RegisterView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
]
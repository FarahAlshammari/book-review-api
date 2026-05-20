from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from .models import Book, Review
from .serializers import (
    BookSerializer,
    ReviewSerializer,
    RegisterSerializer,
    ChangePasswordSerializer
)


# 📚 Books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


# 📝 Reviews
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book_id=book_id)


class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


# 👤 Register
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


# 🔐 Change Password
class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer

    permission_classes = [IsAuthenticated]

    def get_object(self):

        return self.request.user

    def update(self, request, *args, **kwargs):

        user = self.get_object()

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not user.check_password(serializer.data.get("old_password")):

                return Response(

                    {"old_password": "Wrong password"},

                    status=status.HTTP_400_BAD_REQUEST

                )

            user.set_password(serializer.data.get("new_password"))

            user.save()

            return Response(

                {"message": "Password updated successfully"},

                status=status.HTTP_200_OK

            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
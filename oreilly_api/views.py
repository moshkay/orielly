from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BookSerializer
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book
import json


class AllBookView(APIView):
    serializer_class = BookSerializer

    def get(self, request):
        data = request.query_params

        filter = data.get('query')
        fil = data.get("fields")

        page_length = data.get("limit", "100")
        page = data.get("page", 1)
        if filter:
            books = Book.objects.filter(Q(title__icontains=filter) | Q(description__icontains=filter)|
                                        Q(isbn__icontains=filter) | Q(author__icontains=filter),
                                        )
        else:
            books = Book.objects.all()

        books = books.order_by("-id")

        paginator = Paginator(books, int(page_length))
        pager = paginator.get_page(page)
        data = BookSerializer(pager, many=True).data
        next_page = ""
        previous_page = ""
        if pager.has_next():
            next_page = pager.next_page_number()

        if pager.has_previous():
            previous_page = pager.previous_page_number()

        res = {
            "Data": data,
            "Total": books.count(),
            "previous_page": previous_page,
            "next_page": next_page,
            'total_pages': pager.paginator.num_pages,
            'current_page': pager.number
        }
        return Response(res, status=status.HTTP_200_OK)

    def post(self, request):
        body = request.body

        if not body:
            return Response({"status": status.HTTP_401_UNAUTHORIZED, "message": "Request body cannot be empty"},
                            status=status.HTTP_401_UNAUTHORIZED)
        body = body.decode()
        body = json.loads(body)
        if body.get("author"):
            if type(body.get("author")) != list:
                return Response({'error': 'author must be an array of names eg. ["shun li","bob lee"]', 'status': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            body['author'] = str(body['author'])

        serializer = BookSerializer(data=body)
        if serializer.is_valid():
            book = serializer.save()
            return Response({'entity': serializer.data,'message': "Book added successfully",  'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):
    serializer_class = BookSerializer

    def get(self, request, id):
        book = get_object_or_404(Book, pk=id)
        res = BookSerializer(book).data
        return Response({'data':res,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)

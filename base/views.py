from .models import Book, Loan
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from .serializer import BookSerializer, LoanSerializer, RegisterSerializer, UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView


@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['GET'])
def test(req):
    return Response('test')

# Protected view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def member(req):
    return Response({'member':'only'})

@api_view(['POST'])
def login(request):
    return TokenObtainPairView.as_view()(request._request)

# Registration view
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#crud with Serializer for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]
    
# CRUD with Serializer for Book
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

# CRUD with Serializer for Loan
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def borrow(self, request, pk=None):
        book = self.get_object()
        user = request.user
        if book.available_copies > 0:
            loan = Loan.objects.create(user=user, book=book)
            book.available_copies -= 1
            book.save()
            return Response({"message": "Book borrowed successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "No available copies left"}, status=status.HTTP_400_BAD_REQUEST)    

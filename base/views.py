from .models import Book, Loan
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import BookSerializer, LoanSerializer, RegisterSerializer
from rest_framework import status


@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['GET'])
def test(req):
    return Response('test')

#i’m protected
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def member(req):
    return Response({'member':'only'})

# register
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#crud with Serializer for User

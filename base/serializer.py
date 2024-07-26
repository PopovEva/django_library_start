from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Loan


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class LoanSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    book_title = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ['id', 'user', 'book', 'loan_date', 'return_date', 'returned', 'user_name', 'book_title']

    def get_user_name(self, obj):
        return obj.user.username

    def get_book_title(self, obj):
        return obj.book.title  
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id', 'username')        
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user               
    
    
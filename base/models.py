from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    # isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return self.title

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
     



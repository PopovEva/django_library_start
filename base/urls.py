from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'loans', views.LoanViewSet)

urlpatterns = [
    path('', views.index),
    path('test/',views.test),
    path('login/', views.login),  # Обновленный путь для логина
	path('member/',views.member),
    path('register/',views.register),
    path('', include(router.urls)),
]


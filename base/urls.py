from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', views.index),
    path('test/',views.test),
    path('login/', TokenObtainPairView.as_view()),
	path('member/',views.member),
    path('register/',views.register),
    
    # path('products/',views.cars),
    # path('products/<int:id>/',views.cars)
]


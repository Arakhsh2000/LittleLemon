from django.shortcuts import render
from rest_framework.decorators import api_view, api_view, permission_classes
from rest_framework import generics,viewsets,permissions
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html', {})



class MenuItemView(generics.ListCreateAPIView):
      queryset = Menu.objects.all()
      serializer_class = MenuSerializer
      permission_classes = [AllowAny]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
      queryset = Menu.objects.all()
      serializer = MenuSerializer
      permission_classes = [AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
      queryset = Booking.objects.all()
      serializer_class = BookingSerializer
      permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
     return Response({"message":"This view is protected"})      
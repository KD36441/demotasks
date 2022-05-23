from .models import  product
from .serializers import productSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication
class productModelViewSet(viewsets.ModelViewSet):
  queryset = product.objects.all()
  serializer_class = productSerializer
  #authentication_classes=[BasicAuthentication]
  #permission_classes=[IsAuthenticated]
  #permission_classes=[AllowAny]
  permission_classes=[SessionAuthentication]
  permission_classes=[IsAdminUser]
  #permission_classes=[IsAuthenticatedOrReadOnly]
  #permission_classes=[DjangoModelPermissions]


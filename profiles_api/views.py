from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from . import models
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """returns a list of APIViews features"""
        an_apiview = [
           'Uses HTTP Method as function (get, post, patch, put ,delete)',
           'Is similar to a traditional Django view',
           'Gives you the most control over your application logic',
           'Is mapped menually to URLs',   
        ]
        
        return Response({'massage': 'Hello', 'an_apiview': an_apiview}) 
    
    def post(self, request):
        """creates a hello massage with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            massage = f'Hello {name}'
            return Response({'massage': massage})
        else:
            return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
        
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
        
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello massage"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)', 
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        
        return Response({'massage':'Hello', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello massage"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            massage = f'Hello {name}'
            return Response({'massage': massage})
        else:
            return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method': 'GET'})
    
    def upadte(self, request, pk=None):
        """handle updating an object"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """handle upadting part of object"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({'http_method': 'DELETE'})
    
class  UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating profiles"""
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    
class UserLoginApiView(ObtainAuthToken):
    """Handel creating user authentication tiken"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

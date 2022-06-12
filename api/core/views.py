from api.core.models import Usuarios
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UsuarioSerializer


class CreateUsuariosViewSet(viewsets.ModelViewSet):
    """Cria usuarios comuns"""
    permission_classes = ()
    serializer_class = UsuarioSerializer
    queryset = Usuarios.objects.all()



class ListaUsuarios(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UsuarioSerializer   

    def get_queryset(self):
        queryset = Usuarios.objects.all()
        return queryset

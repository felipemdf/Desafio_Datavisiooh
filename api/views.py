from rest_framework import viewsets
from api.models import Pessoa
from api.serializer import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
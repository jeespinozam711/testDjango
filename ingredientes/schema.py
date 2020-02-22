import graphene

from graphene_django.types import DjangoObjectType
from ingredientes.models import Articulo
from graphql_jwt.decorators import login_required


class ArticuloType(DjangoObjectType):
  class Meta:
    model= Articulo

class Query(object):
  all_Productos = graphene.List(ArticuloType,token=graphene.String(required=True))

  @login_required
  def resolve_all_Productos(self, info, **kwargs):
    return Articulo.objects.all()
import graphene
import ingredientes.schema
import graphql_jwt


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Query(ingredientes.schema.Query, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query ,mutation=Mutation)

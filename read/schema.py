import graphene
from graphene_django import DjangoObjectType
from .models import Person

class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("id","first_name","last_name","dob","email","country")

class Query(graphene.ObjectType):

    all_person = graphene.List(PersonType)

    def resolve_all_person(root, info):
        return Person.objects.all()

schema = graphene.Schema(query=Query)
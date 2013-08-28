# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from sharedcontentbaskets.models import SharedContentBasket
from sharedcontentbaskets.models import UserName
from sharedcontentbaskets.models import ContentID
from sharedcontentbaskets.serializers import SharedContentBasketSerializer
from sharedcontentbaskets.serializers import UserNameSerializer
from sharedcontentbaskets.serializers import ContentIDSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from sharedcontentbaskets.crudmanytomanyview import CRUDManyToManyView

class SharedContentBasketList(generics.ListCreateAPIView):
    queryset = SharedContentBasket.objects.all()
    serializer_class = SharedContentBasketSerializer

class SharedContentBasketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SharedContentBasket.objects.all()
    serializer_class = SharedContentBasketSerializer

class SharedContentBasketUserList(CRUDManyToManyView):
    model = SharedContentBasket
    field_name = 'users'
    serializer_class = UserNameSerializer

class SharedContentBasketContentList(CRUDManyToManyView):
    model = SharedContentBasket
    field_name = 'content'
    serializer_class = ContentIDSerializer

class UserList(generics.ListCreateAPIView):
    queryset = UserName.objects.all()
    serializer_class = UserNameSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserName.objects.all()
    serializer_class = UserNameSerializer

class UserLookup(APIView):
    def get(self, request, pk, Format=None):
        try:
	    user = UserName.objects.get(name=pk)
        except UserName.DoesNotExist:
	    raise Http404
	serializer = UserNameSerializer(user)
	return Response(serializer.data)

class UserContentBasketList(APIView):
    def get(self, request, pk, format=None):
	try:
	    user = UserName.objects.get(pk=pk)
	except UserName.DoesNotExist:
	    raise Http404
        baskets = user.sharedcontentbaskets.all()
        serializer = SharedContentBasketSerializer(baskets, many=True)
	return Response(serializer.data)

class ContentList(generics.ListCreateAPIView):
    queryset = ContentID.objects.all()
    serializer_class = ContentIDSerializer

class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentID.objects.all()
    serializer_class = ContentIDSerializer


class ContentLookup(APIView):
    def get(self, request, pk, Format=None):
        try:
            content = ContentID.objects.get(contentid=pk)
        except ContentID.DoesNotExist:
            raise Http404
        serializer = ContentIDSerializer(content)
        return Response(serializer.data)

class ContentContentBasketList(APIView):
    def get(self, request, pk, format=None):
        try:
            content = ContentID.objects.get(pk=pk)
        except ContentID.DoesNotExist:
            raise Http404
        baskets = content.sharedcontentbaskets.all()
        serializer = SharedContentBasketSerializer(baskets, many=True)
        return Response(serializer.data)


class SharedContentBasketAddUser(APIView):
    #model = UserName
    #context_object_name = 'users'
    def post(self, request, pk, field_pk, format=None):
	try: 
	    basket = SharedContentBasket.objects.get(pk=pk)
	except SharedContentBasket.DoesNotExist:
	    raise Http404
        try: 
	    user = UserName.objects.get(pk=field_pk)
        except UserName.DoesNotExist:
	    raise Http404
	basket.users.add(user)
	return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk, field_pk, format=None):
        try:
            basket = SharedContentBasket.objects.get(pk=pk)
        except SharedContentBasket.DoesNotExist:
            raise Http404
        try:
            user = UserName.objects.get(pk=field_pk)
        except UserName.DoesNotExist:
            raise Http404
        basket.users.remove(user)
	return Response(status=status.HTTP_202_ACCEPTED)


class SharedContentBasketAddContent(APIView):
    #model = UserName
    #context_object_name = 'users'
    def post(self, request, pk, field_pk, format=None):
        try:
            basket = SharedContentBasket.objects.get(pk=pk)
        except SharedContentBasket.DoesNotExist:
            raise Http404
        try:
            content = ContentID.objects.get(pk=field_pk)
        except ContentID.DoesNotExist:
            raise Http404
        basket.content.add(content)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk, field_pk, format=None):
        try:
            basket = SharedContentBasket.objects.get(pk=pk)
        except SharedContentBasket.DoesNotExist:
            raise Http404
        try:
            user = ContentID.objects.get(pk=field_pk)
        except ContentID.DoesNotExist:
            raise Http404
        basket.content.remove(content)
        return Response(status=status.HTTP_202_ACCEPTED)


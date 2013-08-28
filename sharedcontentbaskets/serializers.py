from django.forms import widgets
from rest_framework import serializers
from sharedcontentbaskets.models import SharedContentBasket, UserName, ContentID, LANGUAGE_CHOICES, STYLE_CHOICES

class SharedContentBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedContentBasket
        fields = ('id', 'name', 'users', 'content')

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserName
        fields = ('id','name')

class ContentIDSerializer(serializers.ModelSerializer):
    class Meta:
	model = ContentID
	fields = ('id', 'contentid')    

from rest_framework import serializers
from matserver.models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["number", "description","manufacturer", "provider", "user"]

class CarrierSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=False)
    class Meta:
        model = Carrier
        fields = ["uid", "description", "article"]
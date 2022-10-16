from rest_framework import serializers

from ads.models import *


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


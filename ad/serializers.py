from rest_framework import serializers
from .models import Ad


class AdSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ad
        fields = "__all__"
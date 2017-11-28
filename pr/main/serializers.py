from django.contrib.auth import models as auth_models
from rest_framework import serializers

from main import models


class UserAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_models.User
        fields = ("id", "username", "first_name", "last_name", "email")


class AgentSerializer(serializers.ModelSerializer):
    user = UserAgentSerializer()

    class Meta:
        model = models.Agent
        fields = ("user", "role")

    def create(self, validated_data):
        return self.Meta.model.objects.create_with_details(**validated_data)

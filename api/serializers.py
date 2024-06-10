from django.contrib.auth.models import User
from rest_framework import serializers
from . models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["id","username","password"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","tittle","content","created_at"]
        # to no allow writting user
        extra_kwargs = {"author": {"read_only":True}}

class NoteEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content"]
        read_only_fields = ["id", "author", "created_at"]
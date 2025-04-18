from rest_framework import serializers
from .models import NotesModel
from taggit.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class NotesSerializer(serializers.ModelSerializer):
    truncated_body = serializers.SerializerMethodField()
    tags = serializers.ListField(child=serializers.CharField(), required=False, write_only=True)

    class Meta:
        model = NotesModel
        fields = ['id', 'title', 'body', 'truncated_body', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        note = NotesModel.objects.create(**validated_data)

        # Add tags to the note
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            note.tags.add(tag)

        note.save()
        return note

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Serialize the tags into a list of tag names
        representation['tags'] = [tag.name for tag in instance.tags.all()]

        return representation

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        # Clear existing tags and add new tags
        instance.tags.clear()
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)

        return instance

    def get_truncated_body(self, obj):
        # Truncate the body to a fixed number of characters (e.g., 100 characters)
        return obj.body[:100] + "..." if len(obj.body) > 100 else obj.body


class NotesDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = NotesModel
        fields = ['id', 'title', 'body', 'tags']

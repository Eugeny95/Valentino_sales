from rest_framework import serializers


class Action:
    def __init__(self, title, id):
        self.title = title
        self.id = id


class ActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
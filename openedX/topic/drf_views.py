from rest_framework_mongoengine import viewsets
import models.Topic
import serializers.TopicSerializer
class TopicViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.all()
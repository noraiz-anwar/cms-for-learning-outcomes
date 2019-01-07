from rest_framework_mongoengine import serializers
import models.Topic

class TopicSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
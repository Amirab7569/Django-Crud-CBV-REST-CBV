from rest_framework import serializers
from ...models import Post
from django.contrib.auth.models import User

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    
    
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = Post
        fields = ['id','title','body','snippet','author','relative_url','absolute_url','is_published']
        read_only_fields = ['author']
        
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)


    # change data for show
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet',None)
            rep.pop('relative_url',None)
            rep.pop('absolute_url',None)
        else:
            rep.pop('body',None)
        return rep
    
    # create author obj in DataBase
    def create(self, validated_data):
        validated_data['author'] = User.objects.get(pk=self.context.get('request').user.id)
        return super().create(validated_data)
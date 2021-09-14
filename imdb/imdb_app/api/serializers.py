from rest_framework import serializers
from imdb_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        #feild = ['name', wite all field]
        #exclude = ['name', etc etc]

    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Too short")
        else:
            return value







# serial way lenthy but easy
""" class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Too short")
        else:
            return value """
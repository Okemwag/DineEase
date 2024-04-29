from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    rater = serializers.StringRelatedField()
    rating = serializers.CharField(source='get_rating_display')
    comment = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)


    class Meta:
        model = Review
        fields = "__all__"


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ['rater']


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ['rater', 'rating', 'created_at']

class ReviewDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ['rater']





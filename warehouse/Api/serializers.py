from rest_framework import serializers

class UsersSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    class Meta:
        fields = ('username', 'email' )


class RecentPurchaseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    face = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    size = serializers.IntegerField()
    recent = serializers.StringRelatedField(many=True)

    class Meta:
        fields = ('id', 'face', 'price', 'size', 'recent')
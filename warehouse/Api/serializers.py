from rest_framework import serializers



class RecentPurchaseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    face = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    size = serializers.IntegerField()
    recent = serializers.StringRelatedField(many=True)

    class Meta:
        fields = ('id', 'face', 'price', 'size', 'recent')
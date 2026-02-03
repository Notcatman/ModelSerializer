from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField()
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        error_messages={
            "does_not_exist": "Product does not exist",
            "required": "Product is required"
        }
    )

    class Meta:
        model = Review
        fields = ("rating", "product", "content")

    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Rating should be between 1 and 5")
        return value

    # def validate_product(self, value):
    #     if not Product.objects.filter(pk=value).exists():
    #         raise serializers.ValidationError("Product does not exist.")
    #     return value

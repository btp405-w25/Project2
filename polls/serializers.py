from rest_framework import serializers
from .models import DeliveryRating, Vendor  # Import your models

class DeliveryRatingSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(max_length=255)  # Adjust as needed
    rating = serializers.IntegerField(min_value=1, max_value=5)
    review_text = serializers.CharField(style={'base_template': 'textarea.html'})
    delivery_date = serializers.DateField()
    eco_friendly_packaging = serializers.BooleanField()
    image = serializers.ImageField(required=False)  # For image uploads

    class Meta:
        model = DeliveryRating
        fields = ['vendor', 'rating', 'review_text', 'delivery_date', 'eco_friendly_packaging', 'image']

    def create(self, validated_data):
        # Assuming you have a way to get or create the Vendor instance
        vendor_name = validated_data.pop('vendor')
        vendor, created = Vendor.objects.get_or_create(name=vendor_name)
        delivery_rating = DeliveryRating.objects.create(vendor=vendor, **validated_data)
        return delivery_rating
from rest_framework import serializers
from .models import MoringaMerch

class MerchSerializer(serializers.ModelSerializer):
    """
    class faclitates the conversion of MoringaMerch model into a json object
    """
    class Meta:
        model = MoringaMerch
        fields = ('name', 'description', 'price')
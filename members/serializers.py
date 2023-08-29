from rest_framework import serializers
from .models import Organization
from django.contrib.auth.models import User


class OrganizationSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    class Meta:
        model = Organization
        fields = '__all__'
        
    def get_country(self, obj):
    # Returns the country code. Adjust if you need a different representation.
        return obj.country.code


class UserOrganizationSerializer(serializers.ModelSerializer):
    followed_organizations = OrganizationSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'followed_organizations')
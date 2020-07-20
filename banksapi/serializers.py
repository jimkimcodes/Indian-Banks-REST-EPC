from rest_framework import serializers
from .models import Banks, Branches


class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'


class BranchesSerializer(serializers.ModelSerializer):
    bank = BanksSerializer()
    class Meta:
        model = Branches
        fields = ('ifsc', 'branch', 'address', 'city', 'district', 'state', 'bank')
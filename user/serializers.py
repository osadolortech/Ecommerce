from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from store_api.serializers import ChartSerializer
from store_api.models import Chart
from django.db import transaction


class CustomUser(serializers.ModelSerializer):

    chart_items = ChartSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = [
            "id","name","address","Location","city","chart_items"
        ]



class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length = 150)

    @transaction.atomic()
    def save(self, request):
        user=super().save(request)
        user.name = self.data.get('name')
        user.save()
        return user



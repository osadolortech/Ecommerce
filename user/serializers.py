from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from store_api.models import Chart
from django.db import transaction


class CustomUser(serializers.ModelSerializer):

    Chart = Chart()

    class Meta:
        model = User
        fields = [
            "id","name","address","Location","city"
        ]



class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length = 150)

    @transaction.atomic()
    def save(self, request):
        user=super().save(request)
        user.name = self.data.get('name')
        user.save()
        return user



from rest_framework import serializers
from .models import Mascota, Vacunas

class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class VacunasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacunas
        fields = '__all__'

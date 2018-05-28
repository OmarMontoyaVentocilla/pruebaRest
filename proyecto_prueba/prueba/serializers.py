from rest_framework import  serializers


class MiSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    hora_actual=serializers.DateTimeField()

  
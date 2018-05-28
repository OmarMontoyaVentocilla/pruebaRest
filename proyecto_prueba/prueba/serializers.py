from rest_framework import  serializers

#CREO MIS CAMPOS QUE SERAN SERIALIZADOS

class MiSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    hora_actual=serializers.DateTimeField()

  
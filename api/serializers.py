from rest_framework import serializers
from .models import pedido, detalle_pedido

class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = serializers.CharField(source='producto.nombre')

    class Meta:
        model = detalle_pedido
        fields = ('id', 'producto', 'cantidad', 'subtotal')

class PedidoSerializer(serializers.ModelSerializer):
    detalles_pedido = DetallePedidoSerializer(many=True, read_only=True)
    cliente = serializers.CharField(source='cliente.username')
    estado = serializers.CharField(source='estado.descripcion')
    cupon = serializers.CharField(source='cupon.descripcion', allow_null=True)

    class Meta:
        model = pedido
        fields = ('id', 'fecha', 'subtotal', 'igv', 'total', 'cliente', 'estado', 'cupon', 'detalles_pedido')

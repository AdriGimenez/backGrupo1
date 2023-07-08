from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import pedido
from .serializers import PedidoSerializer, DetallePedidoSerializer


class MisComprasAPIView(generics.RetrieveAPIView):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return pedido.objects.filter(cliente_id=pk)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = serializer.data
        detalle_pedido_data = []
        for detalle in instance.detalle_pedido_set.all():
            detalle_serializer = DetallePedidoSerializer(detalle)
            detalle_pedido_data.append(detalle_serializer.data)
        response_data['detalle_pedido'] = detalle_pedido_data
        return Response(response_data)
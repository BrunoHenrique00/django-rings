from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Anel
from .serializers import AnelSerializer

class AnelViewSet(viewsets.ModelViewSet):
    queryset = Anel.objects.all()
    serializer_class = AnelSerializer

    def create(self, request, *args, **kwargs):
        # Custom logic to enforce ring creation rules
        # Count existing rings by type
        elfos_count = Anel.objects.filter(forjadoPor='Elfos').count()
        anoes_count = Anel.objects.filter(forjadoPor='Anões').count()
        homens_count = Anel.objects.filter(forjadoPor='Homens').count()
        sauron_count = Anel.objects.filter(forjadoPor='Sauron').count()

        if request.data['forjadoPor'] == 'Elfos' and elfos_count >= 3:
            return Response({'error': 'Limite de 3 anéis para Elfos excedido.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['forjadoPor'] == 'Anões' and anoes_count >= 7:
            return Response({'error': 'Limite de 7 anéis para Anões excedido.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['forjadoPor'] == 'Homens' and homens_count >= 9:
            return Response({'error': 'Limite de 9 anéis para Homens excedido.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['forjadoPor'] == 'Sauron' and sauron_count >= 1:
            return Response({'error': 'Apenas 1 anel pode ser forjado por Sauron.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)



def index(request):
    return render(request, 'index.html')
from django.shortcuts import render
from rest_framework import viewsets # what is viewsets?
from .models import Apply
from .serializers import *

#CBV

class ApplyViewSet(viewsets.ModelViewSet):
    queryset = Apply.objects.all() # Apply model의 모든 것을 가져다 queryset으로 쓰겠다.
    serializer_class = ApplySerializer # ApplySerializer를 사용하겠다.

from .models import Apply
from rest_framework import serializers # use rest_framework

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__' # make all field serializer
        # fields = ['title', 'body'] make title and body fields serializer 
        #read_only_fields = ('title', ) # tuple recommended / title을 read_only로 만들수 있다.
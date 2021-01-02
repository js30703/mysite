from rest_framework import serializers
from jamo.models import Verbs, Myverbs
from django.contrib.auth.models import User

class VerbsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Verbs
        fields = '__all__'
  
class MyverbsSerializer(serializers.ModelSerializer):
    verbList = VerbsSerializer(many= True )
    
    class Meta: 
        model = Myverbs
        fields = '__all__'
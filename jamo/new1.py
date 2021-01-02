from django.shortcuts import render
from django.db.models import Max
from . jamo1 import A_EOYO
from . models import Verbs
import random

def get_random3():
    max_id = Verbs.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        verbs = Verbs.objects.filter(pk=pk).first()
        if verbs:
            return verbs


    print(A_EOYO('먹다'))
    get_random3()

# Create your views here.

from django.db import models
from django.conf import settings
# Create your models here.

class Verbs(models.Model):
    shape = models.CharField(max_length=200)
    verb_type = models.CharField(max_length=200)
    reguler = models.CharField(max_length=200, blank= True)
    level = models.CharField(max_length=200)
    target_code= models.CharField(max_length=200, blank= True)
    en_w = models.TextField(null=True,default='')
    example = models.TextField(null=True,default='')
    
    def __str__(self):
        return self.shape

class Endings(models.Model):
    shape = models.CharField(max_length=200)
 
class Myverbs(models.Model):
    userpk =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    verbList= models.ManyToManyField(Verbs, related_name='verblist')

    def __str__(self):
        return self.userpk.username
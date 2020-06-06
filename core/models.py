from django.db import models
from django.utils.timezone import now
# Create your models here.


class Member(models.Model):
    id = models.CharField(primary_key= True,blank= False,max_length=100)
    real_name = models.CharField(blank= False,max_length=100)
    tz = models.CharField(blank= False,max_length=100)

    def __str__(self):
        return self.id


class ActivityPeriods(models.Model):
    member= models.ForeignKey(Member,on_delete = models.CASCADE, blank=False, related_name='activity_period')
    start_time = models.DateTimeField(default=now, blank=True)
    end_time = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.member) + " | " + str((self.start_time).strftime("%B %d %Y %I:%M:%S %p"))






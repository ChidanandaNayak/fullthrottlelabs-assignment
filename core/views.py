from django.shortcuts import render
from rest_framework import permissions
from .models import (
    Member,
    ActivityPeriods,
)
from .serializers import (
    ActivitySerializers,
    MemberSerializer,
    MemberCreateSerializer,
    ActivityCreateSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from datetime import  timedelta
from rest_framework import generics
from faker import Faker
import pytz
import random


class FullThrottleAPI(APIView):

    """
    METHOD : GET,
    PARAMS : NONE
    DESCRIPTION: It displays all members and their respective activities in list view
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        queryset = Member.objects.all()
        s_queryset = MemberSerializer(queryset,many = True)
        return Response({'ok':True,'members':s_queryset.data})


def generate_random_alphanumeric():
    return get_random_string(length=9)


class PopulateDB(APIView):
    """
    METHOD : GET
    DESCRIPTION : It populates member and activities tables with data(1:3).
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):

        for _ in range(1):
            fake = Faker()
            id_ = generate_random_alphanumeric()
            user = MemberCreateSerializer(
                data={
                    "id":id_,
                    "real_name":fake.name(),
                    "tz":random.choice(pytz.all_timezones),
                }
            )

            if user.is_valid():
                user.save()
                for i in range(3):
                    activity = ActivityCreateSerializer(data={
                                "member":id_,
                                "start_time":now()+ timedelta(hours= random.randint(1,5)),
                                "end_time":(now() + timedelta(hours= random.randint(6,24))),
                            })
                    if activity.is_valid():
                        activity.save()

        total_members = Member.objects.count()
        total_activities=  ActivityPeriods.objects.count()
        response = {"status":200,"total_members":total_members,"total_activities":total_activities}

        return Response(response)

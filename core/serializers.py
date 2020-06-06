from .models import ActivityPeriods,Member
from rest_framework import serializers


class ActivitySerializers(serializers.ModelSerializer):

    start_time = serializers.DateTimeField(format="%B %d %Y %I:%M:%S %p")
    end_time = serializers.DateTimeField(format="%B %d %Y %I:%M:%S %p")

    class Meta:
        model = ActivityPeriods
        fields = ['start_time','end_time']
    nested_proxy_field = True


class MemberSerializer(serializers.ModelSerializer):
    activity_period = ActivitySerializers(required=True, many=True)

    class Meta:
        model = Member
        fields = ['id','real_name','tz','activity_period']


class MemberCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = "__all__"


class ActivityCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriods
        fields = "__all__"
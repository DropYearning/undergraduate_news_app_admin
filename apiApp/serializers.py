
from rest_framework import serializers
from newsApp import models as m1
from userApp import models as m2


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = m2.UserInfo
        fields = ('uuid', 'username', 'password')



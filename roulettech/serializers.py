from rest_framework import serializers
from .models import Messages, Account, Token
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User



class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id', 'name', 'email', 'message']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password', 'email']

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["token", "created_at", "expires_at", "user_id", "is_used"]


# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     username = serializers.CharField(
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     password = serializers.CharField(min_length=8)

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'],
#              validated_data['password'])
#         return user

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')


#class UserSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = User
        #fields = ["username" "password", "email"]
        #fields = ["name", "email", "password", "country", "phone"]





        
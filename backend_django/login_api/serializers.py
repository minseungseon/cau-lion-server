#2020-04-20 minseung seon created. 
#serializer는 모두 ModelSerializer로 간단히 처리함 

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

#Sign Up 회원가입

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ('id', 'username', 'email')

        
class CreateUserSerializer(serializers.ModelSerializer) :

    # def create(self, validated_data):
    #     username = validated_data['username']
    #     email = validated_data['email']
    #     password = validated_data['password']

    #     user_obj = User(
    #         username = username,
    #         email = email
    #     )

    #     user_obj.set_password(password)
    #     user_obj.save()

    #     return validated_data

    # class Meta:
    #     model = User
    #     fields = [
    #         'username',
    #         'password',
    #         'email',
    #         'is_superuser',
    #     ]

    class Meta:
        model = User
        fields = ("id", "username", "password", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user

#Check Valid Access on Server 접속 유지중인지 확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
        

#Login 로그인
#연결되는 모델이 없기 때문에 serializer로 작성 

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("아이디 혹은 비밀번호가 잘못 되었습니다.")

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        #exclude = ("user_pk", "likelion_number", "email")
        fields = '__all__'
        #read_only = True
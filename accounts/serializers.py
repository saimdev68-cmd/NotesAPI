from rest_framework import serializers
from .models import CustomUser , Profile
from django.utils import timezone
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","email","username","password"]
        extra_kwargs = {
            "password":{"write_only":True}
        }

    def validate_password(self,value):
        validate_password(value)
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop("password",None)
        for attr , value in validated_data.items():
            setattr(instance,attr,value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","email","username","password","is_active","is_staff"]
        extra_kwargs = {"password":{"write_only":True}}

    def validate_password(self,value):
        validate_password(value)
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop("password",None)
        for attr , value in validated_data.items():
            setattr(instance,attr,value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","username","is_active"]
    
    def update(self, instance, validated_data):
        for attr , value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        return instance
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ["id","user","name","date_of_birth","image","bio"]

    def validate_date_of_birth(self, value):
        if value and value > timezone.now().date():
            raise serializers.ValidationError(
                "Date of birth Must be in past"
            )
        return value
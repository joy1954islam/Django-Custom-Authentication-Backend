from rest_framework import serializers


class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField(style={'placeholder': "Username"},
                                     help_text='Please enter your Username')
    email = serializers.CharField(style={'placeholder': "Email"},
                                     help_text='Please enter your Email')
    token = serializers.CharField(style={'placeholder': "Token"},
                                     help_text='Please enter your Token')
    password = serializers.CharField()
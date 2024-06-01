from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer, ChoiceField

User = get_user_model()


class UserSerializer(ModelSerializer):
    status_choices = (
        ("user", "User"),
        ("admin", "Admin"),
        ("superuser", "Superuser"),
    )
    status = ChoiceField(choices=status_choices, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password', 'status']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])

        if validated_data.get('status'):
            status = validated_data.get('status')

            if status == "admin":
                user.is_staff = True
            elif status == "superuser":
                user.is_superuser = True

        user.save()
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.is_superuser:
            representation['status'] = 'superuser'
        elif instance.is_staff:
            representation['status'] = 'admin'
        else:
            representation['status'] = 'user'

        return representation

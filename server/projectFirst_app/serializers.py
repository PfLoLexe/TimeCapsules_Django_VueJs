from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model


userModel = get_user_model()

class SubPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            'id',
            'username',
        ]


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class SidePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'capCount'
        ]


class PersonFriendsListSerializer(serializers.ModelSerializer):
    friends = FriendsSerializer(many=True)

    class Meta:
        model = userModel
        fields = [
            'friends'
        ]

class PersonSerializer(serializers.ModelSerializer):
    #friends = FriendsSerializer(many=True)
    class Meta:
        model = userModel
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'date_joined',
            'email',
            'lastUpdate',
            'capCount',
        ]


class VaultFilesSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField(method_name='get_file_name')

    def get_file_name(self, obj):
        return '{}.{}'.format(obj.filename, obj.extension)

    class Meta:
        model = models.File
        fields = [
            'file',
        ]


class SimpleVaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vault
        fields = [
            'id',
            'name',
            'description',
        ]


class VaultCardSerializer(serializers.ModelSerializer):
    owner = SubPersonSerializer()

    class Meta:
        model = models.Vault
        fields = [
            'id',
            'name',
            'description',
            'owner',
            'eDate',
        ]

class FileSerializer(serializers.ModelSerializer):
    vault_id = serializers.IntegerField(source='vault.id')

    class Meta:
        model = models.File
        fields = [
            'id',
            'vault_id',
            'filename',
            'extension',
            'path',
        ]


class VaultAccessSerializer(serializers.ModelSerializer):
    vault_id = serializers.IntegerField(source='vault.id')
    person_id = serializers.IntegerField(source='person.id')

    class Meta:
        model = models.VaultAccess
        fields = [
            'vault_id',
            'person_id',
            'permissions',
        ]


'''
class VaultAccessSerializer(serializers.ModelSerializer):
    #person = SubPersonSerializer()

    class Meta:
        model = models.VaultAccess
        fields = [
            'id',
            'permissions',
        ]
'''


class VaultSerializer(serializers.ModelSerializer):
    owner = SubPersonSerializer()
    customAccessList = SubPersonSerializer(many=True)
    files = VaultFilesSerializer(source='file_set', many=True)


    class Meta:
        model = models.Vault
        fields = [
            'id',
            'name',
            'description',
            'cDate',
            'eDate',
            'owner',
            'access',
            'customAccessList',
            'text',
            'files'
        ]


class SimpleCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = [
            'id',
        ]


class CommentsSerializer(serializers.ModelSerializer):
    person = SubPersonSerializer()

    class Meta:
        model = models.Comments
        fields = [
            'id',
            'person',
            'commentText',
            'commentDate',
        ]


class PersonCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = userModel
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        ]

    def create(self, validated_data):
        user = userModel(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class VaultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vault
        exclude = [
            'cDate',
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        exclude = [
            'commentDate',
            'subComments',
        ]


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'


class AccessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VaultAccess
        fields = '__all__'


class FriendShipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendShip
        fields = [
            'fromPersonID',
            'toPersonID'
        ]
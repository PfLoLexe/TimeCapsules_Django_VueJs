from rest_framework import generics, permissions, views, exceptions, viewsets
from rest_framework.response import Response
from projectFirst_app import serializers, models
from django.db import models as dj_models
from datetime import datetime, timedelta
from abc import abstractmethod
from django.contrib.auth import get_user_model


class CapsuleCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.VaultCreateSerializer
    queryset = models.Vault.objects.all()


class CapsuleListView_All(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = models.Vault.objects.filter()
    serializer_class = serializers.VaultCardSerializer


class CapsuleListView_Closed(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = models.Vault.objects.filter(eDate__gt=datetime.now())
    serializer_class = serializers.VaultCardSerializer


class CapsuleListView_Opened(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = models.Vault.objects.filter(eDate__lte=datetime.now())
    serializer_class = serializers.VaultCardSerializer


class CapsuleListView_My(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.VaultCardSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk', None)
        data = models.Vault.objects.filter(owner_id=user_pk)
        return data


class CapsuleListView_NotMy(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.VaultCardSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk', None)
        data = models.Vault.objects.exclude(owner_id=user_pk)
        return data


class CapsuleDetailView(generics.RetrieveAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    #queryset = models.Vault.objects.all()
    serializer_class = serializers.VaultSerializer

    def get_object(self):
        queryset = models.Vault.objects.all()
        vault_pk = self.kwargs.get('vault_pk', None)
        user_pk = self.kwargs.get('user_pk', None)
        data = queryset.get(id=vault_pk)
        if(data.access == 'my'):
            if(data.owner_id == user_pk):
                return data
        else:
            return data

class CapsuleUpdateView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = models.Vault.objects.all()
    serializer_class = serializers.VaultSerializer


class CapsuleAccessListView(generics.ListAPIView):
    #permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.VaultAccessSerializer

    def get_queryset(self):
        vault_pk = self.kwargs.get('vault_pk', None)
        queryset = models.VaultAccess.objects.filter(vault_id=vault_pk)
        return queryset


class CapsuleAccessCreateView(generics.CreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AccessCreateSerializer
    queryset = models.VaultAccess.objects.all()


class CapsuleFileListView(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.FileSerializer

    def get_queryset(self):
        vault_pk = self.kwargs.get('vault_pk', None)
        queryset = models.File.objects.filter(vault_id=vault_pk)
        return queryset


class CapsuleFileCreateView(generics.CreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.FileCreateSerializer
    queryset = models.File.objects.all()


class CapsuleCommentsView(generics.ListAPIView):
    serializer_class = serializers.CommentsSerializer

    def get_queryset(self):
        vault_pk = self.kwargs.get('vault_pk', None)
        queryset = models.Comments.objects.filter(vault_id=vault_pk)
        return queryset


class CapsuleCommentCreateView(generics.CreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CommentCreateSerializer
    queryset = models.Comments.objects.all()


class SidePersonDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.SidePersonSerializer

    def get_queryset(self):
        person_pk = self.kwargs.get('pk', None)
        data = models.Person.objects.filter(id=person_pk)
        capsules = models.Vault.objects.filter(owner_id=person_pk)
        data.update(capCount=len(capsules))
        return data


class PersonFriendsList(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PersonFriendsListSerializer

    def get_queryset(self):
        person_pk = self.kwargs.get('pk', None)
        data = models.Person.objects.filter(id=person_pk)
        return data


class PeopleFriendShipAddView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    #queryset = models.FriendShip.objects.all()
    serializer_class = serializers.FriendShipCreateSerializer


class PeopleFriendShipDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    #queryset = models.FriendShip.objects.all()
    serializer_class = serializers.FriendShipCreateSerializer

    def get_object(self):
        queryset = models.FriendShip.objects.all()
        from_person_pk = self.kwargs.get('f_id', None)
        to_person_pk = self.kwargs.get('t_id', None)
        #print(from_person_pk, to_person_pk)
        data = queryset.get(fromPersonID=from_person_pk, toPersonID=to_person_pk)
        return data


class PersonUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = get_user_model()
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

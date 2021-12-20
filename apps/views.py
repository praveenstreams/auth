from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet,mixins
from django.http import JsonResponse
from .serializers import UserData
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User


class USerViewset(mixins.CreateModelMixin,mixins.UpdateModelMixin,GenericViewSet):
    queryset = User.objects.all()


    def get_serializer_class(self):
        if self.action in ['create','update']:
            return UserData

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer_class()(data=request.data,context={'request': self.request})
        if serializer.is_valid():
            user=serializer.save()
            token,created=Token.objects.get_or_create(user=user)
            return JsonResponse( data={'token': token.key})


        else:
            Response(serializer.errors)

    def update(self, request, *args, **kwargs):

        partial = kwargs.pop('partial', False)
        updated_user = self.get_serializer_class()(data=request.data, instance=self.get_object(),
                                                   partial=partial,context={'request': self.request})

        updated_user.is_valid(raise_exception=True)
        user = updated_user.save()
        return Response(
            UserData(instance=user, context={'request': self.request}).data)

    def destroy(self, request, *args, **kwargs):



        super().destroy(request, *args, **kwargs)
        return Response('success')

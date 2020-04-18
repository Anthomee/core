from rest_framework.mixins import CreateModelMixin, ListModelMixin, \
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Skill, SpokenLanguage, User
from .serializers import SkillSerializer, SpokenLanguageSerializer, UserSerializer


class SkillViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin,
                   UpdateModelMixin, ListModelMixin, DestroyModelMixin):

    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class SpokenLanguageViewSet(GenericViewSet, CreateModelMixin,
                            RetrieveModelMixin, UpdateModelMixin,
                            ListModelMixin, DestroyModelMixin):

    serializer_class = SpokenLanguageSerializer
    queryset = SpokenLanguage.objects.all()


class UserViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin,
                  UpdateModelMixin, ListModelMixin, DestroyModelMixin):

    serializer_class = UserSerializer
    queryset = User.objects.all()

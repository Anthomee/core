from app.models import (
    Skill, SpokenLanguage, User, Role, Pronoun,
    LanguageProficiency, SkillProficiency
)
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ['role']


class SkillProficiencySerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillProficiency
        fields = ['id', 'level']


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['proficiency'] = SkillProficiencySerializer(instance.proficiency).data
        return response


class LanguageProficiencySerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageProficiency
        fields = ['id', 'level']


class SpokenLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpokenLanguage
        fields = ['id', 'name', 'proficiency']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['proficiency'] = LanguageProficiencySerializer(instance.proficiency).data
        return response


class PronounSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pronoun
        fields = ['pronoun']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'user_id',
            'role',
            'display_name',
            'about',
            'avatar',
            'skills',
            'pronoun',
            'spoken_languages',
            'timezone',
            'availability'
        ]

# class RequestInterestedMentorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InterestedMentor
#         fields = [
#             'name',
#             'personalised_note',
#             'accepted'
#         ]


# class RequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Request
#         fields = [
#             'skill',
#             'description',
#             'requester'
#         ]

from app.models import Skill, SpokenLanguage, User, RequestInterest, Request
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
    Proficiency = serializers.CharField()

    class Meta:
        model = Skill
        fields = ['name', 'proficiency']


class SpokenLanguageSerializer(serializers.ModelSerializer):
    Proficiency = serializers.CharField()

    class Meta:
        model = SpokenLanguage
        fields = ['name', 'proficiency']


class UserSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    spoken_languages = SpokenLanguageSerializer(many=True)
    Role = serializers.CharField()
    Pronoun = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'user_id',
            'role',
            'display_name',
            'pronoun',
            'about',
            'avatar',
            'skills',
            'pronoun',
            'spoken_languages',
            'timezone',
            'availability'
        ]

    def create(self, validated_data):
        skills_data = validated_data.pop('skills')
        languages_data = validated_data.pop('spoken_languages')

        for skill_data in skills_data:
            Skill.objects.create(**skill_data)
        for language_data in languages_data:
            SpokenLanguage.objects.create(**language_data)

        user = User.objects.create(**validated_data)
        return user


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

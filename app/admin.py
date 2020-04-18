from django.contrib import admin
from .models import User, Skill, SpokenLanguage, Request, RequestInterest


# class UserAdmin (admin.ModelAdmin):
#     readonly_fields = ('user_id',)


# Add user admin function to registered user if need be
admin.site.register(User)
admin.site.register(Skill)
admin.site.register(SpokenLanguage)
admin.site.register(Request)
admin.site.register(RequestInterest)

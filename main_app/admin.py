from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import *

class CustomUserAdmin(BaseUserAdmin):
    list_display = ["id", "username", "email"]
    list_display_links = ["id", "username"]
    search_fields = ["username", "email"]
    list_per_page = 30

    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    ordering = ['-id']

class WaitingUserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "created_at"]
    list_display_links = ["id", "email"]
    search_fields = ["email"]
    list_per_page = 30

class RecommendationAdmin(admin.ModelAdmin):
    list_display = ["id", "recommended_person", "referrer", "email", "created_at"]
    list_display_links = ["id", "recommended_person"]
    list_filter = ["referrer"]
    search_fields = ["recommended_person", "email"]
    list_per_page = 30

class FAQuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "question", "answer"]
    list_display_links = ["id", "question"]
    search_fields = ["question", "answer"]
    list_per_page = 30

admin.site.register(User, CustomUserAdmin)
admin.site.register(WaitingUser, WaitingUserAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(FAQuestion, FAQuestionAdmin)
admin.site.unregister(Group)


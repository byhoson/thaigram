from django.contrib import admin
from .models import Image,Comment,Like


@admin.register(Image)
class AdminImage(admin.ModelAdmin):

    list_display = (
        'caption',
        'location',
        'created_at',
        'updated_at',
        'author'
    )

    list_filter = (
        'location',
        'created_at'
    )

    search_fields = (
        'location',
    )

    ordering = (
        'location',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

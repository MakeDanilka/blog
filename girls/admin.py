from django.contrib import admin
from .models import Post,Profile,Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')

#admin.site.register(Comment, CommentAdmin)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment,CommentAdmin)


# Register your models here.

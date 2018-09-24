from django.contrib import admin
from firstApp.models import Posts, PostsGroup


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'update_date_time',)
    list_editable = ('title',)
    list_display_links = ('update_date_time',)
    list_filter = ('update_date_time', 'create_date_time', 'owner',)
    search_fields = ('title',)


admin.site.register(Posts, PostAdmin)
admin.site.register(PostsGroup)

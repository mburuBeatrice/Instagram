from django.contrib import admin
from .models import Post,Profile

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["name", "lastupdated","timestamp"]
    list_display_links = ["lastupdated"]
    list_editable = ["name"]
    list_filter = ["lastupdated","timestamp"]
    search_fields = ["name","caption"]
    class Meta:
        model = Post
# Register your models here.
admin.site.register(Post,PostModelAdmin)
admin.site.register(Profile)


from django.contrib import admin
from .models import About, Patents
# Register your models here.

admin.site.register(About)

@admin.register(Patents)
class PatentAdmin(admin.ModelAdmin):
    list_display = ('title', 'granted_on', 'category', 'link')
    list_filter = ('category', 'granted_on')
    search_fields = ('title', 'link')
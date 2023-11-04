from django.contrib import admin
from .models import Signature

class SignatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'signature', 'created_at', 'updated_at')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_per_page = 25

admin.site.register(Signature, SignatureAdmin)
from django.contrib import admin
from .models import Profil

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('gender', 'birthday', 'phone', 'mail', 'location', 'website')

admin.site.register(Profil, ProfilAdmin)
from django.contrib import admin
from main.models import Chrip, StopWord, Profile
# Register your models here.

class ChripAdmin(admin.ModelAdmin):
    list_display = ['body', 'bird']
    search_fields = ['body']

admin.site.register(Chrip, ChripAdmin)


class StopWordAdmin(admin.ModelAdmin):
    list_display = ['word']
    search_fields = ['word']

admin.site.register(StopWord, StopWordAdmin)

admin.site.register(Profile)

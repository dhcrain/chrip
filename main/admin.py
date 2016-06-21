from django.contrib import admin
from main.models import Chrip
# Register your models here.

class ChripAdmin(admin.ModelAdmin):
    list_display = ['body', 'bird']
    search_fields = ['body']

admin.site.register(Chrip, ChripAdmin)

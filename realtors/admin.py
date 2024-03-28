from django.contrib import admin
from .models import Realtor
from django.shortcuts import redirect,render

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


    # def get_urls(self):
    #     urls = super().get_urls()
    #     my_urls = [
    #         path('import-realtors/', self.import_realtor_data,name="import_realtors"),
    #     ]
    #     return my_urls + urls

   
admin.site.register(Realtor, RealtorAdmin)

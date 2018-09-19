from django.contrib import admin
from apptest import models
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username','email','signature')
    search_fields = ('username','email')
    list_filter = ('email',)
admin.site.register(models.Account,AccountAdmin)
admin.site.register(models.Article)
admin.site.register(models.Tag)


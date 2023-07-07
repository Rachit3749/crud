from django.contrib import admin
from.models import registration
# Register your models here.
class register(admin.ModelAdmin):
    list_display = ["email"]
admin.site.register(registration,register)
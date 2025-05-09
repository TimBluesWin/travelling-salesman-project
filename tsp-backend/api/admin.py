from django.contrib import admin
from .models import Point

class PointAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

# Register your models here.

admin.site.register(Point, PointAdmin)
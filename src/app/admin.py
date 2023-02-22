from django.contrib import admin
from app.models import Menu
from app.form import MenuForm


class TreeInline(admin.StackedInline):
    model = Menu
    form = MenuForm


class TreeAdmin(admin.ModelAdmin):
    inlines = [TreeInline]
    form = MenuForm


admin.site.register(Menu, TreeAdmin)

from django.contrib import admin
from .models import Producto, Imagen, Documento
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = "Panel Administración Python"
admin.site.site_title = "Panel Admin!!!!"
admin.site.index_title = "Panel de control."

class ImagenInLine(admin.TabularInline):
    model = Imagen
    extra = 1


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock',)
    search_fields = ('nombre',)
    list_filter = ('categoria',)
    inlines =[ImagenInLine]


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name')
    search_fields = ('email',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Producto, ProductAdmin)
admin.site.register(Imagen)
admin.site.register(Documento)

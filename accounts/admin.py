# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Kustomisasi tampilan model user bawaan
from .models import CustomUser  # Model user kustom

# Kelas kustom untuk mengatur tampilan dan pengelolaan model CustomUser di admin panel
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')  # Kolom utama yang ditampilkan
    list_filter = ('user_type', 'is_staff', 'is_active')  # Filter untuk mempermudah penyaringan data
    search_fields = ('username', 'email')  # Fitur pencarian berdasarkan username dan email
    ordering = ('username',)  # Urutan default data berdasarkan username

    # Konfigurasi tampilan formulir edit user di admin panel
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),  # Informasi dasar
        ('Permissions', {'fields': ('is_staff', 'is_active')}),  # Hak akses
        ('Groups', {'fields': ('groups', 'user_permissions')}),  # Grup dan izin
        ('Informasi Pribadi', {'fields': ('first_name', 'last_name', 'user_type')}),  # Informasi tambahan
    )

    # Konfigurasi formulir tambah user baru
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # Tampilan formulir lebih lebar
            'fields': ('username', 'email', 'password1', 'password2', 'user_type', 'is_staff', 'is_active')},
        ),
    )

# Mendaftarkan model CustomUser ke admin panel
admin.site.register(CustomUser, CustomUserAdmin)

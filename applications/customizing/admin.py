from django.contrib import admin
from .models import UserRole


class UserRoleAdmin(admin.ModelAdmin):
    readonly_fields   = ('created', 'modified')
    list_display      = ('role', 'post_users', 'created', 'modified')
    filter_horizontal = ['users']

    def post_users(self, obj):
        return ', '.join([u.username for u in obj.users.all().order_by('username')])
    
    post_users.short_description = 'Usuarios'


admin.site.register(UserRole, UserRoleAdmin)


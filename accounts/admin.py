from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """관리자 페이지 커스터마이징"""
    
    list_display = ['email', 'name', 'university', 'grade', 'is_active', 'created_at']
    list_filter = ['is_active', 'is_staff', 'university', 'grade']
    search_fields = ['email', 'name', 'student_id']
    ordering = ['-created_at']
    
    fieldsets = (
        ('인증 정보', {'fields': ('email', 'password')}),
        ('개인 정보', {'fields': ('name', 'bio', 'avatar')}),
        ('대학 정보', {'fields': ('university', 'department', 'student_id', 'grade')}),
        ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('중요한 일자', {'fields': ('created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        ('필수 정보', {
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
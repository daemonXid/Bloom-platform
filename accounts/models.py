from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """커스텀 유저 매니저"""
    
    def create_user(self, email, password=None, **extra_fields):
        """일반 사용자 생성"""
        if not email:
            raise ValueError('이메일은 필수입니다')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # 비밀번호 해싱
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """관리자 생성"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """대학생 특화 사용자 모델"""
    
    # 기본 인증 정보
    email = models.EmailField('이메일', unique=True)
    name = models.CharField('이름', max_length=50)
    
    # 대학 정보
    university = models.CharField('대학교', max_length=100, blank=True)
    department = models.CharField('학과', max_length=100, blank=True)
    student_id = models.CharField('학번', max_length=20, blank=True)
    grade = models.IntegerField('학년', null=True, blank=True)
    
    # 프로필
    bio = models.TextField('자기소개', blank=True)
    avatar = models.ImageField('프로필 사진', upload_to='avatars/', blank=True)
    
    # 권한
    is_active = models.BooleanField('활성화', default=True)
    is_staff = models.BooleanField('스태프', default=False)
    
    # 타임스탬프
    created_at = models.DateTimeField('가입일', default=timezone.now)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'  # 로그인 시 email 사용
    REQUIRED_FIELDS = ['name']  # createsuperuser 시 필수 입력
    
    class Meta:
        db_table = 'users'
        verbose_name = '사용자'
        verbose_name_plural = '사용자들'
    
    def __str__(self):
        return f"{self.name} ({self.email})"
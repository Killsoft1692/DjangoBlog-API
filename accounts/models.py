from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, is_active=False, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Email is needed')

        if not password:
            raise ValueError('Password is needed')

        if not name:
            raise ValueError('Name is needed')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.name = name
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, password):

        user = self.create_user(
            email,
            name,
            password=password,
            is_active=True,
            is_staff=True
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(
            email,
            name,
            password=password,
            is_active=True,
            is_staff=True,
            is_admin=True
        )
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def set_staff(self):
        self.staff = True
        return None

    @property
    def is_admin(self):
        return self.admin

    @property
    def set_admin(self):
        self.admin = True
        return None

    @property
    def is_active(self):
        return self.active

    @property
    def set_active(self):
        self.active = True
        return None


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    country = models.CharField(max_length=256, default='')
    city = models.CharField(max_length=256, default='')
    birthday = models.DateField()

    def __str__(self):
        return self.user.name



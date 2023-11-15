from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, email, password=None, name=None, photo=None ):
        if not email:
            raise ValueError("Users must have email addres")

        user = self.model(
            email=email,
            name=name,
            photo=photo

        )
        user = self.model(email=self.normalize_email(email), name=name, photo=photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

  def create_superuser(self, email, password):
        user = self.create_user(
            email, password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    #username = models.CharField(max_length=30, unique=False, default='')
    name = models.CharField(max_length=251, unique=False, blank=False, default='no_name')
    photo  = models.ImageField(blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    updade_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

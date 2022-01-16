from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.utils.models import Entity


class EmailAccountManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('user must have email')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class EmailAccount(AbstractUser, Entity):
    username = models.NOT_PROVIDED
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_website = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null = True , blank= True)
    male = 'male'
    female = 'female'
    gender = models.CharField('title', max_length=255, choices=[
        (male, male),
        (female, female),
    ], null=True , blank=True)
    height = models.IntegerField(null = True , blank= True)
    weight = models.IntegerField(null=True, blank=True)
    calorie_intake = models.IntegerField(null = True, blank= True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = EmailAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
    @property
    def total_calorie(self):
        if self.gender == 'male':
            total_calorie = self.weight * 10 + self.height * 6.25 - self.age * 5 + 5
        else:
            total_calorie = self.weight * 10 + self.height * 6.25 - self.age * 5 - 161
        return total_calorie

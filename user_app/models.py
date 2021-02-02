from django.db import models
from django.contrib.auth.models import User
import random
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code =  models.CharField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.user) + "\t" +str(self.code)
    

    
    
# str(User.first_name) + str(User.last_name) + str(random.Random(uuid.uuid1().hex).getrandbits(128))[0:6]
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# import uuid

# from django.db.models import signals
# from user_app.tasks import send_verification_email

# class UserAccountManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('Email address must be provided')

#         if not password:
#             raise ValueError('Password must be provided')

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields['is_staff'] = True
#         extra_fields['is_superuser'] = True

#         return self._create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     REQUIRED_FIELDS = []
#     USERNAME_FIELD = 'email'
#     email = models.EmailField('email', unique=True, blank=False, null=False)
#     full_name = models.CharField('full name', blank=True, null=True, max_length=400)
#     is_staff = models.BooleanField('staff status', default=False)
#     is_active = models.BooleanField('active', default=False)
#     is_superuser = models.BooleanField('super user', default=False)
#     is_verified = models.BooleanField('verified', default=False)  # Add the `is_verified` flag
#     verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)
#     # User._meta.get_field('email')._unique = True
#     objects = UserAccountManager()

#     def get_short_name(self):
#         return self.email

#     def get_full_name(self):
#         return self.email

#     def __unicode__(self):
#         return self.email



# def user_post_save(sender, instance, signal, *args, **kwargs):
#     if not instance.is_verified:
#         # Send verification email
#         send_verification_email.delay(instance.pk)

# signals.post_save.connect(user_post_save, sender=User)

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


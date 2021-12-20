from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='get_profile',on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    place=models.CharField(max_length=100)


    def __str__(self):
        return f"{str(self.user)}: {self.first_name}"

    @classmethod
    def user_create_profile(cls, user):
        cls.objects.create(user=user)

    @classmethod

    def user_create_profile_signal_reciever(cls, sender, instance, created, *args, **kwargs):
        if created:
            cls.user_create_profile(instance)


models.signals.post_save.connect(UserProfile.user_create_profile_signal_reciever, sender=User)

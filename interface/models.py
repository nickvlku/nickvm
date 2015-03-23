from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class PhoneNumber(models.Model):
    phone_number = PhoneNumberField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone_number)

    def __unicode__(self):
        return self.__str__()


class Call(models.Model):
    sid = models.CharField(max_length=64)
    status = models.CharField(max_length=12)
    from_number = PhoneNumberField(blank=True)
    to_number = PhoneNumberField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class VoiceMail(models.Model):
    audio_file_link = models.URLField()
    originating_call = models.ForeignKey(Call)
    created_on = models.DateTimeField(auto_now_add=True)


class Greeting(models.Model):
    phone_number = models.ForeignKey(PhoneNumber)
    active = models.BooleanField(default=True)
    originating_call = models.ForeignKey(Call)
    created_on = models.DateTimeField(auto_now_add=True)
    audio_file_link = models.URLField()

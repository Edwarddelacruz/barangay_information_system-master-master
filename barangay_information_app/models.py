from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Purok(models.Model):
    id = models.AutoField(primary_key=True)
    purok_number = models.CharField(max_length=50)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Household(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    purok_id = models.ForeignKey(Purok, on_delete=models.CASCADE, default=1)
    place_of_birth = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100)
    civil_status = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    members_of_the_family = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Officials(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    position = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    officials_id = models.ForeignKey(Officials, on_delete=models.DO_NOTHING)
    attendance_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    officials_id = models.ForeignKey(Officials, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    complainant_full_name = models.CharField(max_length=255)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    civil_status = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    purok_number = models.CharField(max_length=50)
    address = models.TextField()
    report_date = models.CharField(max_length=255)
    report_message = models.TextField()
    report_status = models.TextField()
    defendant_full_name = models.CharField(max_length=255)
    defendant_age = models.CharField(max_length=50)
    defendant_gender = models.CharField(max_length=50)
    defendant_civil_status = models.CharField(max_length=50)
    defendant_citizenship = models.CharField(max_length=50)
    defendant_occupation = models.CharField(max_length=50)
    defendant_purok_number = models.CharField(max_length=50)
    defendant_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationOfficials(models.Model):
    id = models.AutoField(primary_key=True)
    officials_id = models.ForeignKey(Officials, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance, address="")


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()

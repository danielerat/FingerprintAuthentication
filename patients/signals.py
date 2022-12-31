from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Patriarch,Family
# When A patriarch Gets Added, add him to a family ! 
@receiver(post_save, sender=Patriarch)
def create_profile(sender, instance, created, **kwargs):
    if created:
        patriarch = instance
        profile = Family.objects.create(
            chief=patriarch,
            nationalId=patriarch.nationalId,
            firstName=patriarch.firstName,
            lastName=patriarch.lastName,
            dob=patriarch.dob,
            sex=patriarch.sex,
            email=patriarch.email,
            phone=patriarch.phone,
        )
        
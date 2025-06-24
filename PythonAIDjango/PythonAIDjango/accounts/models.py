from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    links = models.URLField(max_length=200, blank=True, null=True)
    media = models.FileField(upload_to='media/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    is_following = models.BooleanField(default=False)
    is_followed = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_muted = models.BooleanField(default=False)
    is_verified_email = models.BooleanField(default=False)
    is_verified_phone = models.BooleanField(default=False)
    is_verified_identity = models.BooleanField(default=False)
    is_verified_address = models.BooleanField(default=False)
    is_verified_document = models.BooleanField(default=False)
    is_verified_profile = models.BooleanField(default=False)
    is_verified_account = models.BooleanField(default=False)
    is_verified_payment = models.BooleanField(default=False)
    is_verified_subscription = models.BooleanField(default=False)
    is_verified_membership = models.BooleanField(default=False)
    is_verified_subscription_plan = models.BooleanField(default=False)
    is_verified_payment_method = models.BooleanField(default=False)
    is_verified_transaction = models.BooleanField(default=False)
    is_verified_order = models.BooleanField(default=False)
    is_verified_review = models.BooleanField(default=False)
    is_verified_rating = models.BooleanField(default=False)
    is_verified_comment = models.BooleanField(default=False)
    is_verified_feedback = models.BooleanField(default=False)
    is_verified_notification = models.BooleanField(default=False)
    is_verified_message = models.BooleanField(default=False)
    is_verified_chat = models.BooleanField(default=False)
    is_verified_group = models.BooleanField(default=False)
    is_verified_event = models.BooleanField(default=False)
    is_verified_post = models.BooleanField(default=False)
    is_verified_story = models.BooleanField(default=False)
    is_verified_media = models.BooleanField(default=False)
    is_verified_file = models.BooleanField(default=False)
    is_verified_link = models.BooleanField(default=False)
    is_verified_image = models.BooleanField(default=False)  



    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
post_save.connect(save_user_profile, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    instance.profile.delete()
post_save.connect(delete_user_profile, sender=User)
def update_user_profile(sender, instance, **kwargs):
    instance.profile.save()        
post_save.connect(update_user_profile, sender=User)
def get_user_profile(user):
    try:
        return user.profile
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_id(user_id):
    try:
        return Profile.objects.get(user_id=user_id)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_username(username):
    try:
        return Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_email(email):
    try:
        return Profile.objects.get(user__email=email)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_phone(phone):
    try:
        return Profile.objects.get(phone=phone)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_address(address):
    try:
        return Profile.objects.get(address=address)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_date_of_birth(date_of_birth):
    try:
        return Profile.objects.get(date_of_birth=date_of_birth)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_created_at(created_at):
    try:
        return Profile.objects.get(created_at=created_at)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_updated_at(updated_at):
    try:
        return Profile.objects.get(updated_at=updated_at)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_images(images):
    try:
        return Profile.objects.get(images=images)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_links(links):

    try:
        return Profile.objects.get(links=links)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_media(media):
    try:
        return Profile.objects.get(media=media)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_is_active(is_active):
    try:
        return Profile.objects.get(is_active=is_active)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_is_verified(is_verified):
    try:
        return Profile.objects.get(is_verified=is_verified)
    except Profile.DoesNotExist:
        return None
def get_user_profile_by_is_admin(is_admin):
    try:
        return Profile.objects.get(is_admin=is_admin)
    except Profile.DoesNotExist:
        return None
    
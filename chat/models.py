from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver
from django.db.models import Q
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64
from hashlib import sha256
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    pic=models.ImageField(upload_to="img",blank=True,null=True,default="D:/Django/Chat_App/chatapp/static/img/profile.png")
    friends=models.ManyToManyField("Friend",related_name="myfriends",blank=True)
    
    def __str__(self):
        return self.name
    def add_friend(self, username):
        friend_user = User.objects.filter(username=username).first()
        if friend_user:
            friend_profile, created = Friend.objects.get_or_create(profile=friend_user.profile)
            self.friends.add(friend_profile)
            friend_user.profile.friends.add(Friend.objects.get_or_create(profile=self)[0])
            return True
        else:
            return False
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Friend(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.profile.name
    

        return latest_message
   
class ChatMessage(models.Model):
    
    body=models.TextField(blank=True)
    msg_sender=models.ForeignKey("Profile", on_delete=models.CASCADE,related_name="msg_sender")
    msg_receiver=models.ForeignKey("Profile", on_delete=models.CASCADE,related_name="msg_receiver")
    timestamp = models.DateTimeField(editable=False,default=timezone.now) 
    sender_deleted = models.BooleanField(default=False)
    seen=models.BooleanField(default=False)
   
    
            
    def __str__(self):
        return self.body
    

            

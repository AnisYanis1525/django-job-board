from django.db import models



from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey("City",related_name='user_name', on_delete=models.CASCADE, blank=True, null=True)
    number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile/') 
    
    def __str__(self) -> str:
        return str(self.user)
    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return str(self.name)
        
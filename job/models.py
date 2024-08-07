from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

JOB_TYPE = (
    ('Full time', 'full time'),
    ('Part time', 'part time'),
)

def img_upload(instance, filename):
    image_name, extension = filename.split('.')
    return 'job/%s.%s'% (instance.id, extension)
    pass

class Job(models.Model):
    owner =models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField(max_length=200)
    published_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    image = models.ImageField( upload_to=img_upload)
    slug = models.SlugField(blank=True, null=True)
    
    
    def __str__(self) :
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title) 
        super(Job, self).save(*args, **kwargs)
    
    
    
    
class Category(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self) -> str:
        return self.name   
    
class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField()
    cv = models.FileField(upload_to="apply/")
    letter = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.name  
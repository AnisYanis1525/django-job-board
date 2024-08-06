from django.db import models

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
    title = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField(max_length=200)
    published_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    image = models.ImageField( upload_to=img_upload)
    
    def __str__(self) :
        return self.title
    
    
    
    
class Category(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self) -> str:
        return self.name   
    
    
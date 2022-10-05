from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Birds(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_bird = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Adding in new column for user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
# one to many relationship
class Habitat(models.Model):
    name = models.CharField(max_length = 150, default='unknown')
    location = models.CharField(max_length = 150)
    birds = models.ForeignKey(Birds, on_delete=models.CASCADE, related_name='habitats')

    def __str__(self):
        return self.name

# many to many relationship

class Zoo(models.Model):
    title = models.CharField(max_length=150)
    #this is going to create the many to many relationship and join table
    birds = models.ManyToManyField(Birds)

    def __str__(self):
        return self.title
    

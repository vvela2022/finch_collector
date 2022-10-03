from django.db import models

# Create your models here.
class Birds(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_bird = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Habitat(models.Model):
    name = models.CharField(max_length = 150, default='unknown')
    location = models.CharField(max_length = 150)
    birds = models.ForeignKey(Birds, on_delete=models.CASCADE, related_name='habitats')

    def __str__(self):
        return self.name
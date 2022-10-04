from django.contrib import admin
from .models import Birds, Habitat, Zoo

# Register your models here.
admin.site.register(Birds)
admin.site.register(Habitat)
admin.site.register(Zoo)
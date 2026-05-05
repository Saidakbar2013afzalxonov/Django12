from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import uuid

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    slug = models.SlugField(unique=True, blank=True)
    picture=models.ImageField(upload_to='media/', blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.username)}-{uuid.uuid4().hex[:4]}"
            # base_slug = slugify(f"{self.first_name}-{self.last_name}")
            # unique_id = str(uuid.uuid4())[:4]
            # self.slug = f"{base_slug}-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.

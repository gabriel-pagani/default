from django.db import models
import string, random

def generate_slug():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class Link(models.Model):
    original_url = models.URLField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} -> {self.original_url}"

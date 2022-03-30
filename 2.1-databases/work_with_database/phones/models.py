from django.core.validators import MinValueValidator
from django.db import models
from slugify import slugify

class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.CharField(max_length=500)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(default=None)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)



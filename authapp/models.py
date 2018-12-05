from django.db import models

# Create your models here.
class Sample(models.Model):

    username = models.CharField(
    max_length=20,
    )
    password = models.CharField(
        max_length=20,
    )
    class Meta:
        db_table='Sample'
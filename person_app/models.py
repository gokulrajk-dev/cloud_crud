from django.db import models


class Person(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    address = models.TextField()

    photo = models.ImageField(
        upload_to="person_photos/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
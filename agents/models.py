from django.db import models


class Editor(models.Model):

    name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    bio = models.TextField()

    image = models.ImageField(upload_to='editors/')

    instagram = models.URLField()

    posts = models.CharField(max_length=20, default='0')

    followers = models.CharField(max_length=20, default='0')

    following = models.CharField(max_length=20, default='0')

    project_image = models.ImageField(
        upload_to='projects/images/',
        blank=True,
        null=True
    )

    project_video = models.FileField(
        upload_to='projects/videos/',
        blank=True,
        null=True
    )

    project_description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    subject = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
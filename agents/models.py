# agents/models.py

from django.db import models


# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.brand_name


# Project Model
class Project(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Collecting', 'Collecting'),
        ('Editing', 'Editing'),
        ('Completed', 'Completed'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    project_name = models.CharField(max_length=200)

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


# Media Upload Model
class Media(models.Model):

    MEDIA_TYPE = (
        ('Photo', 'Photo'),
        ('Video', 'Video'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE
    )

    file = models.FileField(upload_to='media_files/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.media_type


# Edited Content Model
class EditedContent(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    edited_video = models.FileField(upload_to='edited_videos/')

    caption = models.TextField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.project_name


# Social Media Post Model
class SocialMediaPost(models.Model):

    PLATFORM_CHOICES = (
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('YouTube', 'YouTube'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES
    )

    post_link = models.URLField()

    posted_date = models.DateField()

    def __str__(self):
        return self.platform
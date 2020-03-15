from django.db import models

class Apply(models.Model):
    name = models.CharField(max_length=50)
    school_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    tech_stack = models.TextField(blank=True, null=True)
    motivation = models.TextField(blank=True, null=True)
    idea = models.TextField(blank=True, null=True)
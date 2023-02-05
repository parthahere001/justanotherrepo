from django.db import models

class Questions(models.Model):
    question_name = models.CharField(max_length=200, blank=False)
    opti1 = models.CharField(max_length=200, blank=False)
    opti2 = models.CharField(max_length=200, blank=False)
    opti3 = models.CharField(max_length=200, blank=False)
    opti4 = models.CharField(max_length=200, blank=False)
    ans = models.CharField(max_length=200, blank=False)


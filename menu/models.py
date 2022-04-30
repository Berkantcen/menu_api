from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    sub_message = models.CharField(max_length=200)


    def __str__(self):
        return self.name
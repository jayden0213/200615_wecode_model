from django.db import models
from user.models import Users

class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    comment = models.CharField(max_length=200)

    class Meta:
        db_table = "comments"



# Create your models here.

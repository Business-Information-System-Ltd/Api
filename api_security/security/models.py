from django.db import models


class Budget(models.Model):
    Budget_code = models.CharField(max_length=10, unique=True)
    Budget_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Budget_code} - {self.Budget_name}"
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Data(models.Model):
      detail = models.CharField(max_length=250)
      patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
      date_created = models.DateTimeField(default=timezone.now)
      
      def __str__(self):
          return f"{self.patient.first_name} {self.patient.last_name} report ({self.detail})"
      
      def get_absolute_url(self):
          return reverse("data_detail")
      
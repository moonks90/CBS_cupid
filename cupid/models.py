from django.db import models

# Create your models here.
class person(models.Model):
    gsb_id = models.CharField(max_length=20)
    mate1_id = models.CharField(max_length=20)
    mate2_id = models.CharField(max_length=20)
    mate3_id = models.CharField(max_length=20)

    def __str__(self):
        return self.gsb_id + '/' + self.mate1_id + '/' + self.mate2_id + '/' + self.mate3_id


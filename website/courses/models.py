from django.db import models

# Create your models here.

class Course(models.Model):
    tag = models.CharField(max_length=1)
    row = models.IntegerField()
    col = models.IntegerField()

    def _str_(self):
        return self.tag + ' @(' + str(self.row) + ',' + str(self.col) + ')'

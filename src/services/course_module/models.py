from django.db import models


# Create your models here.
class CourseActivity(models.Model):
    activity_name = models.CharField(max_length=100)
    has_groups = models.BooleanField()

    class Meta:
        db_table = "course_activities"
        app_label = "course_module"
        app_name = "course_module"
        managed = False
        db_alias = "sample_db"

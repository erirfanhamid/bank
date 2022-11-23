from django.db import models
class Assignee(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
class Bug_sheet(models.Model):
    bug_id = models.IntegerField(default=0)
    bug = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    bug_detail = models.CharField(max_length=100, blank=True, null=True)
    assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE)
    def __str__(self):
        return self.bug
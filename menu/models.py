from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=255, null=True, blank=True)
    named_url = models.CharField(max_length=255, null=True, blank=True)

    def str(self):
        return self.name

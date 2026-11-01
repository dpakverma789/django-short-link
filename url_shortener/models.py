from django.db import models

class UrlMapping(models.Model):
    original_url = models.URLField(max_length=2000, db_index=True)
    short_code = models.CharField(max_length=10, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

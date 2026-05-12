from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.

class Note(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="notes")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False)
    pinned_time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.is_pinned:
            if self.pinned_time is None:
                self.pinned_time = timezone.now()
        else:
            self.pinned_time = None
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["-is_pinned","-pinned_time","-created_at"]
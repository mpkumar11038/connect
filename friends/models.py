from django.conf import settings
from django.db import models


class FriendRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,
                              choices=(('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')),
                              default='pending')

    class Meta:
        unique_together = ('from_user', 'to_user')
        indexes = [
            models.Index(fields=['from_user', 'to_user']),
        ]

    def __str__(self):
        return f"From {self.from_user} to {self.to_user} - {self.status}"

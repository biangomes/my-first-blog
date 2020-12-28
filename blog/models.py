from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
        Post: nome do modelo
        models.Model: significa que o Post é um modelo de Django, então Django
        sabe que ele deve ser salvo no banco de dados
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        __str__() : recebe uma string
        """
        return self.title
    
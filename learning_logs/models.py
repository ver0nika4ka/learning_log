from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model.""" 
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    # A foreign key is a term, code connects each entry to a specific topic.
    # on_delete=if topic deleted, all the entries delete cascading.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # Field doesn’t need size limit, we don’t want to limit the size of entries.
    text = models.TextField()
    # Attribute allows to present entries in the order they were created.
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Attribute uses Entries when it needs to refer to more than one entry.
        verbose_name_plural = 'entries'

    # Which information to show when it refers to individual entries.
    def __str__(self):
        """Return a string representation of the model."""
        string_representation = self.text
        # Entry can be long text, we tell to use first 50 characters.
        if len(string_representation) > 50:
            string_representation = f"{self.text[:50]}..."
        return string_representation


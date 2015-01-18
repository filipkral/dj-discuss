from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    summary = models.TextField()
    description = models.TextField()
    
    def __unicode__(self):
        return '[S %s] %s' % ( self.pk , self.title )

class Comment(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, related_name='comments')
    owner = models.ForeignKey('auth.User', related_name='comments')
    
    def __unicode__(self):
        return '[C %s] %s' % ( self.pk , self.title )
    
    class Meta:
        ordering = ['created',] # always order by date
    

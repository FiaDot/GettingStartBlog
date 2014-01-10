from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    # under python 3.0
#    def __unicode__(self):
#        return self.title
    
    # over python 3.0
    def __str__(self):
        return self.title

    
    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)
    
    def __str__(self):
        return "%s : %s" % (self.post, self.body[:60])
    
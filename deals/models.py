from django.db import models

class Deal(models.Model):
    def __unicode__(self):
        return "{} from {}".format(self.heading, self.provider)
    provider=models.CharField(max_length=100)
    heading=models.CharField('Subject', max_length=100)
    description=models.TextField(max_length=200)
    poster=models.ImageField(upload_to='images')
    url=models.CharField(max_length=50)
    pub_date=models.DateTimeField('Date Published')
    exp_date=models.DateTimeField('Expires On')
    like_count=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    



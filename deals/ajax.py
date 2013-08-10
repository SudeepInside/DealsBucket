from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def dojob(request):
    return simplejson.dumps({'text':'Do you really like this'})

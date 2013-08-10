from django.http import HttpResponse
from django.template import Context, loader
from deals.models import Deal

def index(request):
    deal_bucket=Deal.objects.all()
    template=loader.get_template('deals/index.html')
    context=Context({'deal_bucket':deal_bucket})
    return HttpResponse(template.render(context))

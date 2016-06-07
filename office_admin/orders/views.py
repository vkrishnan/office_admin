#from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from .forms import OrderForm
from .models import Order

def order_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                                         user = request.user,
                                         name = form.cleaned_data['name'],
                                         category = form.cleaned_data['category'],
                                         order_date = timezone.now(),
                                         status = 'Pending'
                                         )
            order.save()
            return HttpResponseRedirect('/order/success/')
    else:
        form = OrderForm()
        
    variables = RequestContext(request, {
                            'form': form})
                         
    return render_to_response(
                'order.html', variables)
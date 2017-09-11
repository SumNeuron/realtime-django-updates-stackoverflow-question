from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from time import sleep
from django.utils import timezone



from .models import MyQuery
from .forms import MyForm

from .tasks import add


# index view contains the basic form
def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            clean_data = form.cleaned_data

            query = MyQuery()
            query.a = clean_data['a']
            query.b = clean_data['b']
            query.date = timezone.now()
            query.save()

            return HttpResponseRedirect(reverse('my_app:query', args=(query.id,)))

        else:
            context = {'form': form}
            return render(request, 'my_app/index.html', context)

    else:
        form = MyForm()
        context = {'form': form}
        return render(request, 'my_app/index.html', context)




# query view displays the results
def query(request, query_id):
    query = get_object_or_404(MyQuery, pk=query_id)

    # if the result isnt ready
    if query.total == 0:
        # Create Async task to do some computation
        # add(query.a, query.b).delay()
        pass

    # in the mean time take user to the results page
    context = {"status": "status goes here"}
    return render(request, 'my_app/query.html', context)

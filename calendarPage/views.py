# from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin

# from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic

# from braces.views import SelectRelatedMixin

# from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(generic.ListView):
    model = models.Events
    template_name = "calendarPage/calendarPage_base.html"
    # select_related = ("user", "group")


def event(request):
    all_events = Events.objects.all()
    get_event_types = Events.objects.only('event_type')

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:  
        event_arr = []
        if request.GET.get('event_type') == "all":
            all_events = Events.objects.all()
        else:   
            all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.event_name
            start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,
        "get_event_types":get_event_types,

    }
    return render(request,'admin/poll/event_management.html',context)
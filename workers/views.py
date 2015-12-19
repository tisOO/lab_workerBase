# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from django.views.generic.base import View
from django.http import Http404, HttpResponseRedirect

from .models import Worker, WorkerChild, JobPosition, USER_TYPES
from web_navig.utils import Breadcrumb

# Create your views here.


class ViewWorkers(View):

    template_name = None
    request = None

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')

        return super(ViewWorkers, self).dispatch(request, *args, **kwargs)

    def get_context_data(self):

        view = None
        if self.request.user.user_type == "Admin":
            view = ViewWorkersAdmin()
        return view

    def get(self, request):
        view = self.get_context_data()
        return view.get(self.request)


class ViewWorkersAdmin(View):

    template_name = 'workers_list/admin.html'

    NAVIGATION = [
        Breadcrumb("/workers/", "Список работников"),
        Breadcrumb("/departments/", "Список департаментов"),
    ]

    def get_context_data(self):
        workers = Worker.objects.filter()
        for worker in workers:
            try:
                job = JobPosition.objects.filter(worker_id=worker.id)[0]
            except IndexError:
                pass
            else:
                workers[worker.id].department = job.department
                workers[worker.id].position = job.position
        return {
            "workers": workers,
            "navigation": self.NAVIGATION
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render_to_response(self.template_name, context, context_instance=RequestContext(request, processors=[]))


# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from workers.utils import get_all_models, get_model_by_name, get_model_fields
from workers.form import get_form


def workers_processor(request):
    """A context processor that provides model data."""
    return {
        'names_list': get_all_models().keys()
    }


def index(request):
    return render_to_response('base.html',
                              context_instance=RequestContext(request,
                                                              processors=[workers_processor]))


def display(request, cur_model_name):
    names_list = get_all_models().keys()

    if cur_model_name not in names_list:
        raise Http404("Page does not exist")

    current_model = get_all_models().get(cur_model_name)
    fields = get_model_fields(current_model)
    form = get_form(current_model, fields)
    all_entries = current_model.objects.all().values()

    inter_dic = dict()
    for dic in all_entries:
        inter_dic[dic.get(u'id')] = {k: v for k, v in dic.items() if k != u"id"}

    full_dic = dict()
    for guid, data in inter_dic.items():
        out_dic = dict()
        f_list = list()
        for k, v in data.items():
            inner_dic = dict()
            type_dic = dict()
            inner_dic[k] = v
            type_dic[fields.get(k)] = inner_dic
            f_list.append(type_dic)
        full_dic[guid] = f_list
    return render_to_response('display.html',
                              context_instance=RequestContext(request,
                                                              locals(),
                                                              processors=[workers_processor]))


def add_new(request, cur_model_name):
    if request.method == "POST":
        current_model = get_model_by_name(cur_model_name)
        fields = get_model_fields(current_model)
        form = get_form(current_model, fields)

        if form(request.POST).is_valid():
            form(request.POST).save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "Data was saved.")
            return redirect('/workers/'+cur_model_name)
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 "Data was not saved. Check please and try again.")
            return redirect('/workers/'+cur_model_name)
    else:
        raise Http404("Page does not exist")


def ajax_update(request, cur_model_name):
    if request.method == "POST":
        guid = request.POST['guid']
        value = request.POST['value']
        field = request.POST['field']
        args = {field: value}
        current_model = get_model_by_name(cur_model_name)
        current_model.objects.filter(pk=guid).update(**args)
        return HttpResponse()
    else:
        raise Http404("Page does not exist")

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from feedback.forms import FeedbackForm
from .models import Feedback

def index(request):
    feedback_list = Feedback.objects.order_by("-data_publi")[:5]
    template = loader.get_template("feedback/index.html")
    context = {
        "feedback_list": feedback_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, feedback_id):
    try:
        feedback = Feedback.objects.get(pk=feedback_id)
    except Feedback.DoesNotExist:
        raise Http404("Feedback não existe")
    return render(request, "feedback/detail.html", {"feedback": feedback})

def create_feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(data = request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Deu merda")

    
    context = {'form': form}
    return render(request, "feedback/create_feedback.html", context)

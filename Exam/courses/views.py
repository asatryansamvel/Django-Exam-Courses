from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.db.models import F
from django.urls import reverse
from django.views import generic

from .models import Course

class IndexView(generic.ListView):
    template_name = "courses/index.html"
    context_object_name = "courses_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Course.objects.all()

class DetailView(generic.DetailView):
    model = Course
    template_name = "courses/detail.html"

class RateView(generic.DetailView):
    model = Course
    template_name = "courses/rate.html"

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "courses/detail.html", {"course": course})

def vote(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        r = request.POST.get('vote')
    course.rate = (course.count * course.rate + int(r)) / (course.count + 1)
    course.count += 1
    course.save() # this will update only

    return HttpResponseRedirect(reverse("courses:detail", args=(course.id,)))

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course


class CourseObjectMixin:
    model = Course
    lookup = 'course_id'  # id

    def get_object(self):
        course_id = self.kwargs.get(self.lookup)
        obj = None
        if course_id is not None:
            obj = get_object_or_404(self.model, id=course_id)
        return obj


class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'

    # CourseObjectMixin
    # def get_object(self):
    #     course_id = self.kwargs.get('course_id')
    #     obj = None
    #     if course_id is not None:
    #         obj = get_object_or_404(Course, id=course_id)
    #     return obj

    def get(self, request, course_id=None):
        context = dict()
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, course_id=None):
        context = dict()
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')

        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'

    # def get_object(self):
    #     course_id = self.kwargs.get('course_id')
    #     obj = None
    #     if course_id is not None:
    #         obj = get_object_or_404(Course, id=course_id)
    #     return obj

    def get(self, request, course_id=None):
        context = dict()
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
            form = CourseModelForm(instance=obj)
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, course_id=None):
        context = dict()
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self, request):
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()  # reset the form
        context = {'form': form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request):
        course_context = {
            'object_list': self.get_queryset()
        }
        return render(request, self.template_name, course_context)


# Base View Class = View
class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'

    def get(self, request, course_id=None):
        # context = dict()
        # if course_id is not None:
        #     obj = get_object_or_404(Course, id=course_id)
        #     context['object'] = obj
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)


# HTTP Methods
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})

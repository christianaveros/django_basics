from django.shortcuts import render
from django.views.generic import View

from .models import Note


class Index(View):
	template_name = 'notes/index.html'

	def get_context_data(self):
		context = {
			'notes':Note.objects.order_by('-title'),
		}
		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data()
		return render(request, self.template_name, context)
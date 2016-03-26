from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import QuestionForm

# Create your views here.
def index(request):
	"""Display homepage"""
	if request.method != 'POST':
		# No data submitted. Create blank form
		form = QuestionForm()
	else:
		# POST data submitted; process data
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('answer_app:success'))
			
	context = {'form': form}
	return render(request, 'answer_app/index.html', context)
	
def success(request):
	"""Display question submitted page"""
	return render(request, 'answer_app/success.html')

from django.shortcuts import render

# Create your views here.
def index(request):
	"""Display homepage"""
	return render(request, 'answer_app/index.html')

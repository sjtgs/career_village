from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse
from .models import Photo
from .forms import PhotoForm
from django.utils import timezone
from .filters import PhotoFilter

#from .models import Post
# Create your views here.

#Home page Career Village
def home(request):
	photos_lists = Photo.objects.all()
    return render(request, 'web/photo_list.html', {'photos': photos_lists})




#upload and crop function
class dashboardView(View):
    def get(self, request):
	        photos_lists = Photo.objects.all()
	        return render(self.request, 'web/dashboard.html', {'photos': photos_lists})

    def post(self, request):
        #time.sleep(1)
		form = PhotoForm(self.request.POST, self.request.FILES)
		if form.is_valid():
			    #photo = request.user
	          	    photo = form.save()
		    	    photo.uploaded_at = timezone.now()
	                    data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
		else:
		        data = {'is_valid': False}
		return JsonResponse(data)

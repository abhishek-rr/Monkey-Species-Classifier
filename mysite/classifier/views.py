from fastai.learner import load_learner
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from classifier.forms import ImageForm
from django.core.files.storage import default_storage
from django.conf import settings
import os

class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self, request):
        form = ImageForm()
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = ImageForm(request.POST)
        if form.is_valid():
            f = request.FILES['Submit_image']
            file_save = default_storage.save("pic",f)
            file_url = default_storage.url(file_save)
            ImagePath = os.path.join(settings.BASE_DIR, file_url[1:])
            learn_inf = load_learner('assets/Monkeyexport.pkl')
            prediction = learn_inf.predict(ImagePath)[0]
        else:
            prediction = "Invalid Request"
        return render(request, "home.html", {'prediction': prediction})    

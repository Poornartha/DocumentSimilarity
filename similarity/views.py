from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms

# Imaginary function to handle an uploaded file.
from .operations import similarity_check


def home(request):
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
        	tar1 = form.cleaned_data.get('target1')
        	tar2 = form.cleaned_data.get('target2')
        	ft1 = form.cleaned_data.get('filetype1')
        	ft2 = form.cleaned_data.get('filetype2')
        	print(ft1)
        	output = similarity_check(request.FILES['file1'], request.FILES['file2'], tar1, tar2, ft1, ft2)
        	return render(request, 'templates/upload.html', {'form': form, 'output': output})
    else:
    	form = forms.UploadFileForm()
    return render(request, 'templates/upload.html', {'form': form})

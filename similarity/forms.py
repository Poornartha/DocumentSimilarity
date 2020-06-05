from django import forms


choices = (("1", "csv"),("2", "excel"))


class UploadFileForm(forms.Form):
	file1 = forms.FileField()
	file2 = forms.FileField()
	target1 = forms.CharField(max_length=50)
	target2 = forms.CharField(max_length=50)
	filetype1 = forms.ChoiceField(choices=choices)
	filetype2 = forms.ChoiceField(choices=choices)

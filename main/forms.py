from main.models import Game , CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm



    ###########################################################
    ######################## USER FORMS #######################
    ###########################################################

class CustomUserCreationForm(UserCreationForm):
	def __init__(self,*args,**kwargs):
		super(CustomUserCreationForm,self).__init__(*args,**kwargs)
		#del self.fields['username']

	class Meta:
		model = CustomUser
		fields = ('email',)

class CustonUserChangeForm(UserChangeForm):
	def __init__(self,*args,**kwargs):
		super(CustonUserChangeForm,self).__init__( *args, **kwargs)
		    #del self.fields['username']

	class Meta:
		model = CustomUser
		fields = '__all__'


class CustomUserLoginForm(forms.Form):
	email = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())



class EditProfileForm(forms.ModelForm):
	class Meta:
		model =CustomUser
		fields=['first_name','last_name','email']


    ###########################################################
    ######################## GAME FORMS #######################
    ###########################################################

class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


    ###########################################################
    ######################## FEEDBACK FORMS #######################
    ###########################################################

 

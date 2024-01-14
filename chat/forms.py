from django import forms
from django.forms import ModelForm
from .models import ChatMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
class ChatMessageForm(ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={"class":"forms","rows":3,"placeholder":"Type Your Message Here"}))
    class Meta:
        model=ChatMessage
        fields=["body"]

class SignUpForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'sforms'})
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

      
        if username and password1 and password1.lower().startswith(username.lower()):
            raise forms.ValidationError("Password is too similar to the username.")

        
        if password1 and len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("User with this username already exists.")

        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
    
from django.contrib.auth import authenticate
    
class LoginForm(AuthenticationForm):
   
    class Meta:
        model = User
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'sforms'})
    def get_user(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

       
        user = authenticate(username=username, password=password)

        return user
        


class AddFriendForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"sforms","rows":3,"placeholder":"Type Username Here"}))

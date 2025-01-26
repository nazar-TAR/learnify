
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control custom_input', 'placeholder': ' Your username'}), label='login')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control custom_input', 'placeholder': ' Your password'}), label='password')
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class': 'form-control custom_input', 'placeholder': ' Your username'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control custom_input', 'placeholder': ' Your email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control custom_input', 'placeholder': ' Your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control custom_input', 'placeholder': ' Your last name'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control custom_input', 'placeholder': ' Your password'}))
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control custom_input', 'placeholder': ' Your password'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        else:
            return email


from datetime import datetime

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username', disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    this_year = datetime.today().year
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-5))))


    class Meta:
        model = get_user_model()
        fields = ('photo', 'username', 'email', 'date_of_birth', 'first_name', 'last_name')
        labels= {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'photo': 'Photo',
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-input'}),
        }
from django import forms

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['fav_bird', 'photo']

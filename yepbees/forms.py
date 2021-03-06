from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    contact_phone = forms.CharField(required=True,max_length=13, min_length=9,
            widget=forms.TextInput(attrs={
                'class':'form-control' , 'pattern':'[0-9]+',
                 'title':'Enter numbers Only.',
                 'placeholder': 'Your phone number'
             }))
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = "Your name"
        self.fields['from_email'].label = "Your email"
        self.fields['contact_phone'].label = "Phone number"
        self.fields['message'].label = "Your message"

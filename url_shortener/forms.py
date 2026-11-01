from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class URLShortenerForm(forms.Form):
    original_url = forms.URLField(
        label='URL',
        required=True,
        widget=forms.URLInput(attrs={
            'placeholder': 'Paste your long URL here...',
            'required': 'required',
            'class': 'url-input'
        }),
        error_messages={
            'required': 'Please enter a URL.',
            'invalid': 'Please enter a valid URL.'
        }
    )

    def clean_original_url(self):
        url = self.cleaned_data.get('original_url')
        
        # Additional validation checks
        if not url or not url.strip():
            raise ValidationError('URL cannot be blank.')
        
        # Check for potentially dangerous protocols
        dangerous_protocols = ['javascript:', 'data:', 'vbscript:', 'file:']
        url_lower = url.lower()
        for protocol in dangerous_protocols:
            if url_lower.startswith(protocol):
                raise ValidationError('Invalid URL protocol.')
        
        # Ensure URL has a scheme
        if not url_lower.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        return url

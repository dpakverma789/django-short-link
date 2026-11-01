from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import UrlMapping
from .forms import URLShortenerForm
import random
import string
import qrcode
import base64
from io import BytesIO

def create_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def url_shortener(request):
    context = {}
    if request.method == 'POST':
        form = URLShortenerForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            try:
                short_code = UrlMapping.objects.get(original_url=original_url).short_code
            except UrlMapping.DoesNotExist:
                while True:
                    short_code = create_short_code()
                    if not UrlMapping.objects.filter(short_code=short_code).exists():
                        break
                UrlMapping.objects.create(short_code=short_code,original_url=original_url)
            short_url = request.build_absolute_uri(f"/{short_code}/")
            context["short_url"] = short_url
            
            # Generate QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(short_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Convert to base64 for display in template
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            qr_code_data = base64.b64encode(buffer.getvalue()).decode()
            context["qr_code"] = f"data:image/png;base64,{qr_code_data}"
        else:
            context["form_errors"] = form.errors
    else:
        form = URLShortenerForm()
    
    context["form"] = form
    return render(request,'url_shortener/index.html',context=context)


def redirect_url(request,short_code):
    try:
        url = UrlMapping.objects.get(short_code=short_code)
    except UrlMapping.DoesNotExist:
        raise Http404("Short URL does not exist.")
    return redirect(url.original_url)
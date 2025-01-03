from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CateringForm

@csrf_exempt
def catering(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = CateringForm(request.POST)
        if form.is_valid():
            catering_request = form.save()
            
            # Send an email notification to the restaurant
            subject = 'New Catering Request Received'
            message = (
                f"New catering request details:\n\n"
                f"Name: {catering_request.full_name}\n"
                f"Phone: {catering_request.phone}\n"
                f"Date: {catering_request.date}\n"
                f"Number of Persons: {catering_request.number_of_person}\n"
                f"Catering Type: {catering_request.get_catering_type_display()}\n"
                f"Location: {catering_request.location}\n"
                f"Email: {catering_request.email}\n\n"
                "Please review the catering request and respond accordingly.\n\n"
                "Best regards,\n"
                "Henom Restaurant"
            )
            recipient_email = 'info@henomrestaurant.com'
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
            
            return JsonResponse({'message': 'Catering request successful!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = CateringForm()
    return render(request, 'catering.html', {'form': form})

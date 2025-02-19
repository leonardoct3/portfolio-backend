from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import Client
from send_email import send_email

# Create your views here.

@api_view(['POST'])
def send(request):
    if request.method == 'POST':
        # Use request.data for DRF's Request object
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        # Print for debugging
        print("Received:", name, email, message)

        # Save to your Client model (adjust fields as needed)
        client = Client.objects.create(name=name, email=email, message=message)
        client.save()

        # Construct the body of the email
        body = f"""
        <html>
            <body>
            <h2>New message from your portfolio</h2>
            <br>
            <p><strong>Name:</strong> {name}</p>
            <br>
            <p><strong>Email:</strong> {email}</p>
            <br>
            <p><strong>Message:</strong> {message}</p>
            </body>
        </html>
        """

        send_email("leocarvalhoteixeira@gmail.com", body, "New message from your portfolio")

        # Return a JSON response indicating success
        return Response({"message": "Email sent successfully"})
  
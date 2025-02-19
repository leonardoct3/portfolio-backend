import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To, From, Content
from dotenv import load_dotenv
load_dotenv()


def send_email(email: str, content: str, subject: str = "No subject"):
    api_key = os.environ.get("SENDGRID_API_KEY")
    
    print("API key:", api_key)

    sendgrid_client = SendGridAPIClient(api_key)

    message = Mail(
        from_email=From(email="leocarvalhoteixeira@gmail.com", name="Leo"),
        to_emails=[To(email=email)],
        subject=subject,
        html_content=content  
    )

    sendgrid_client.send(message)

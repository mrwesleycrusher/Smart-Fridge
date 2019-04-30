import smtplib, ssl

def send_to_email(reciever_email, message):
    port = 465  # For SSL
    password = input("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()
    sender_email = "CS370.Lamborghini@gmail.com"

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("CS370.Lamborghini@gmail.com", "nickwestylermax")
        # TODO: Send email here
        server.sendmail(sender_email,reciever_email,message)


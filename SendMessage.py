import smtplib, ssl
import Food

def send_to_email(reciever_email, message):
        port = 465  # For SSL
        password = input("Type your password and press enter: ")

            # Create a secure SSL context
        context = ssl.create_default_context()
        sender_email = "CS370.Lamborghini@gmail.com"

        # Send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("CS370.Lamborghini@gmail.com", "nickwestylermax")
                server.sendmail(sender_email,reciever_email,message)

def get_the_message(foods):
        message = "Hello User-Senpai!\nI have created you a grocery list!\n*Noitices your bulge (in your wallet)* uwu what's that?\n\n"
        count = 1
        for x in foods:
                message+=str(count)
                message+=x.get_count()
                message+=" "
                message+=x.get_name()
                message+="s\n"             
        return message

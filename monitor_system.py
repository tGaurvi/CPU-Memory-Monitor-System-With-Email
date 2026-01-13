import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -----------------------
# Email Sending Function
# -----------------------

def send_email_alert(subject, message):
    sender_email = "gaurvitiwari3@gmail.com"
    sender_password = "fvkq nmyg ljyf vyws"
    receiver_email = "gaurvitiwari3@gmail.com"

    msg = MIMEMultipart()
    msg["From"]= sender_email
    msg["To"]= receiver_email
    msg ["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    # Connecting the server
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error in sending email", e)



def check_system_health ():
    cpu_threshold= int(input("Enter CPU threshold value:- "))
    memory_threshold= int(input("Enter memory threshold value:- "))

    current_cpu= psutil.cpu_percent(interval=1)
    current_memory= psutil.virtual_memory()

    print("Current CPU usage is:- ", current_cpu)

    print("Current Virtual Memory is:- ", current_memory)

    if cpu_threshold > current_cpu:
        print("Emergency! Sent an email to the admin")
        send_email_alert(
            subject= "High CPU Alert",
            message= f"Cpu usage is High"

        )
    else:
        print("Cpu is fine")
    
    if current_memory.available < memory_threshold  :
        print("Emergency! Sent an email to the admin")
        send_email_alert("Memory Alert", "Memory usage is high")
    else:
        print("Everything is fine")

check_system_health()
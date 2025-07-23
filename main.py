import smtplib
import  random
import datetime as dt

email = "rehan020344@gmail.com"
password = "phhy hmxo pxsb blzx"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

def send_email(message_to_send):
    connection.login(user=email , password=password)
    connection.sendmail(from_addr=email ,
                        to_addrs="rehan020345@yahoo.com",
                        msg=f"Subject:Qoute of the day \n\n{message_to_send} "
                        )
def qoute():
    with open("quotes.txt" , "r") as file :
        file_data = file.read().splitlines()
        return random.choice(file_data)


current_time = dt.datetime.now()
today = current_time.weekday()
if today == 2:
    send_email(qoute())
    print("Email sent")
else:
    print("Today is not Wedneday")


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

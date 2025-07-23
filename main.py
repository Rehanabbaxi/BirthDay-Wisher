# import smtplib
# import  random
# import datetime as dt

# email = "rehan020344@gmail.com"
# password = "majj upjc ryjf wvsb"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()

# def send_email(message_to_send):
#     connection.login(user=email , password=password)
#     connection.sendmail(from_addr=email ,
#                         to_addrs="rehan020345@yahoo.com",
#                         msg=f"Subject:Qoute of the day \n\n{message_to_send} "
#                         )
# def qoute():
#     with open("quotes.txt" , "r") as file :
#         file_data = file.read().splitlines()
#         return random.choice(file_data)


# current_time = dt.datetime.now()
# today = current_time.weekday()
# if today == 2:
#     send_email(qoute())
#     print("Email sent")
# else:
#     print("Today is not Wedneday")


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import smtplib
import  random
from datetime import  datetime


Email = "rehan020344@gmail.com"
Password = "majj upjc ryjf wvsb"


df = pd.read_csv("birthdays.csv")
current_day = datetime.now().day
current_month = datetime.now().month

matched_date = df[ (df["month"] == 7) & (df["day"] == 23)]
email_of_receiver = matched_date["email"].values[0]
name_of_receiver  = matched_date["name"].values[0]

if len(matched_date) >0 :

    random_letter = random.choice(["letter_1.txt" , "letter_2.txt" , "letter_3.txt"])

    with open(f"letter_templates/{random_letter}" , "r") as file :
        letter_to_send = file.read()
        letter_to_send = letter_to_send.replace("[NAME]" , name_of_receiver)
        letter_to_send = letter_to_send.replace("Angela" ,  "Rehan")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=Email , password=Password)
        connection.sendmail(from_addr=Email ,
                            to_addrs=email_of_receiver,
                            msg=f"Subject:Happy Birthday \n\n{letter_to_send}"
                            )
    print("Email sent")

else :
    print("No birthday today")
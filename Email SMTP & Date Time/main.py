import smtplib
import datetime as dt
import random
import pandas
import csv

# Hosted on PythonAnywhere


today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv('Birthdays.csv')

birthday_dict = {(data_row["Month"], data_row["Day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["Name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="chanduguntur4444@gmail.com", password="Chandu@4444")
        connection.sendmail(
            from_addr="chanduguntur4444@gmail.com",
            to_addrs=birthday_person["Email"],
        msg=f"Subject:Happy Birthday\n\n{contents}")














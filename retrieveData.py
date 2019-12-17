import csv
import datetime

from send_mail import *


def send_mails(file_path):
    birthdays = open_file(file_path)

    if len(birthdays) != 0:
        for x in birthdays:
            send_mail(x[0], x[3], email_message(x[0]))


def open_file(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        friends = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if is_birth_day_today(get_current_date(), date(row[2])):
                    friends.append((row[0], row[1], row[2], row[3]))

                line_count += 1

        return friends


def is_birth_day_today(current_date, birth_date):
    decomposed_current_date = current_date.split("/")
    decomposed_birth_date = birth_date.split("/")
    if decomposed_birth_date[1] == decomposed_current_date[1] and decomposed_birth_date[2] == decomposed_current_date[2]:
        return True
    else:
        return False

def get_current_date():
    date = datetime.datetime.now()
    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")

    return year + "/" + month + "/" + day


def email_message(first_name):
    return ("happy birthday, dear "+ first_name)

def date(date_of_birth):
    date = date_of_birth.split("/")
    if date[1] == "02":
        if date[2] == "29":
            return date[0] + "/" + date[1] + "/28"
    else:
        return date_of_birth

#open_file("/Users/marius/Documents/PyCharm/CodingChallenge/Birthdays.csv")

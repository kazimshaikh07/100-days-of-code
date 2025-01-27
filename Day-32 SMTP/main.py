# import smtplib
#
# my_gmail = "kazimshaikh210342@acropolis.in"
# password = "urnd cnvb ygsh movj"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_gmail, password= password)
#     connection.sendmail(from_addr=my_gmail,to_addrs="kazimshaikh210342@acropolis.in", msg="subject:hello\n\nthis is main body line")
#
import datetime

now = datetime.datetime.now()
print(now)

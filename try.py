import smtplib

mail=smtplib.SMTP("smtp.gmail.com",587)
mail.starttls()
mail.login("highskyairlines@gmail.com", "tbaznscvfshdsnqo")
message="Hi this is Pragyan"
user = input("please enter your email: ")
mail.sendmail("highskyairlines@gmail.com", user, message)
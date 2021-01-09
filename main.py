from popup import window

# read metadata from file
person = "Rachuj"
file = "Hausaufgaben.pdf"

# read mail template from file
f = open("mail_template.txt", 'r')

msg_mail = f.read()
msg_mail = msg_mail.format(person, file)

f.close

# wait for new file in folder

# ask user to send
win = window(msg_mail, "Hausaufgaben.pdf", "Rachuj")

win.popup()
print(win.ed_msg_mail)
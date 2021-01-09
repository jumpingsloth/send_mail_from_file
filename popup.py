from tkinter import *

class window:

	def __init__(self, usr_msg_mail, usr_file, usr_person):
		self.msg_mail = usr_msg_mail
		self.file = usr_file
		self.person = usr_person
		self.ed_msg_mail = ''

	def popup(self):

		def exit_gui(send):
			if send:
				self.ed_msg_mail = mail.get(1.0, "end-1c")
				root.destroy()
			else:
				self.output = FALSE
				root.destroy()
		
		# root
		root = Tk()
		root.title("Sending Message")
		root.resizable(False, False)

		# heading
		msg = f"Sending email with {self.file} to {self.person}."

		message = Label(root, text=msg, font='none 13 bold')
		message.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

		# message
		mail = Text(root, height=20, width=40)
		mail.grid(row=1, column=0, columnspan=4, pady=10)
		mail.insert(INSERT, self.msg_mail)

		mail.focus()
		mail.tag_add(SEL, "1.12", "1.25")
		mail.mark_set(INSERT, "1.12")
		mail.see(INSERT)

		# buttons
		empty1 = Label(root, text='')
		empty1.grid(row=2, column=0)

		button2 = Button(root, text="Cancel", command= lambda: exit_gui(False))
		button2.grid(row=2, column=1, pady=10)

		button1 = Button(root, text="Send", font="none 10 bold", command= lambda: exit_gui(True))
		button1.grid(row=2, column=2, pady=10)

		empty2 = Label(root, text='')
		empty2.grid(row=2, column=3)

		# root
		root.mainloop()

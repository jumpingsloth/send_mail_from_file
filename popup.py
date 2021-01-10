from tkinter import *

from read_data import Data

class Window:

	def __init__(self, usr_file):
		self.data = Data()


		self.file = usr_file
		self.person = ''
		self.msg_mail = self.data.read_template(self.person, self.file)

		self.adress_to = ''
		self.subject = ''

		self.ed_msg_mail = ''

	def popup(self):

		# root
		root = Tk()
		root.title("Sending Message")
		root.resizable(False, False)

		def exit_gui(send):
			if send:
				self.adress_to = to.get()
				self.subject = subject.get()
				self.ed_msg_mail = mail.get(1.0, "end-1c")
				root.destroy()
			else:
				self.ed_msg_mail = False
				self.subject = False
				self.adress_to = False
				root.destroy()
		
		def enter_person(keystroke):
			self.person = to.get()
			msg.set(f"Sending email with {self.file} to {self.person}\n")
			root.update_idletasks

			self.msg_mail = self.data.read_template(self.person, self.file)
			mail.delete(1.0, END)
			mail.insert(INSERT, self.msg_mail)
			
			self.adress_to = self.data.read_adress_to(self.person)
			to.delete(0, END)
			to.insert(INSERT, self.adress_to)

		# heading
		msg = StringVar()
		msg.set(f"Sending email with {self.file} to _____\n")

		message = Label(root, textvariable=msg, font='none 13 bold')
		message.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

		# from
		from_label = Label(root, text="From:")
		from_label.grid(row=1, column=0, columnspan=1)

		from_adress = Entry(root, width=40)
		from_adress.grid(row=1, column=1, columnspan=3, pady=10, padx=20)
		from_adress.insert(INSERT, self.data.adress_from)

		# to
		to_label = Label(root, text="To:")
		to_label.grid(row=2, column=0, columnspan=1)

		to = Entry(root, width=40)
		to.grid(row=2, column=1, columnspan=3, pady=10, padx=20)
		to.bind('<Return>', enter_person)

		# subject
		subject_label = Label(root, text="Subject:")
		subject_label.grid(row=3, column=0, columnspan=1)

		subject = Entry(root, width=40)
		subject.grid(row=3, column=1, columnspan=3, pady=10, padx=20)
		subject.insert(INSERT, self.file)

		# message
		mail = Text(root, height=20, width=40, pady=10, padx=10)
		mail.grid(row=4, column=0, columnspan=4, pady=10, padx=20)
		mail.insert(INSERT, self.msg_mail)

		mail.focus()
		mail.tag_add(SEL, "1.12", "1.24")
		mail.mark_set(INSERT, "1.12")
		mail.see(INSERT)

		# buttons
		empty1 = Label(root, text='')
		empty1.grid(row=5, column=0)

		button2 = Button(root, text="Cancel", command= lambda: exit_gui(False))
		button2.grid(row=5, column=1, pady=10)

		button1 = Button(root, text="Send", font="none 10 bold", command= lambda: exit_gui(True))
		button1.grid(row=5, column=2, pady=10)

		empty2 = Label(root, text='')
		empty2.grid(row=5, column=3)

		# root
		root.mainloop()

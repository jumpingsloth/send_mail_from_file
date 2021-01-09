from tkinter import *

def gui(msg_mail):

	def exit_gui(send):
		if send:
			output = mail.get(1.0, "end-1c")
			print(output)
			root.destroy()
			return output
		else:
			root.destroy()
			return False

	# root
	root = Tk()
	root.title("Sending Message")
	root.resizable(False, False)

	# heading
	file = "some_file.pdf"
	person = "Some Person"
	msg = f"Sending email with {file} to {person}."

	message = Label(root, text=msg, font='none 13 bold')
	message.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

	# message
	mail = Text(root, height=20, width=40)
	mail.grid(row=1, column=0, columnspan=4, pady=10)
	mail.insert(INSERT, msg_mail)

	mail.focus()
	mail.tag_add(SEL, "1.12", "1.25")
	mail.mark_set(INSERT, "1.12")
	mail.see(INSERT)

	# buttons
	empty1 = Label(root, text='').grid(row=2, column=0)

	button2 = Button(root, text="Cancel", command= lambda: exit_gui(False))
	button2.grid(row=2, column=1, pady=10)

	button1 = Button(root, text="Send", font="none 10 bold", command= lambda: exit_gui(True))
	button1.grid(row=2, column=2, pady=10)

	empty2 = Label(root, text='').grid(row=2, column=3)

	# root
	root.mainloop()

if __name__ == "__main__":
	msg_mail = "Sehr geehrte<r> <andrede> Rachuj,\n\nanbei"
	print(gui(msg_mail))
	
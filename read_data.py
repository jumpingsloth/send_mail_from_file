class Data:

	def read_template(self, person, file):
		# read mail template from file
		f = open("mail_template.txt", 'r')

		msg_mail = f.read()
		msg_mail = msg_mail.format(person, file)

		f.close

		return msg_mail

	def read_adress_from(self):
		return "adress@from.com"

	def read_adress_to(self, person):
		return "adress@to.com"
	

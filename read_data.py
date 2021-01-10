import toml

class Data:

	def __init__(self):
		self.config = toml.load('config.toml')
		self.dir = self.config["userconfig"]["directory"]
		
		self.host = self.config["userconfig"]["host"]
		self.port = self.config["userconfig"]["port"]
		self.adress_from = self.config["userconfig"]["adress"]
		self.password = self.config["userconfig"]["password"]

	def read_template(self, person, file):
		# read mail template from file
		f = open("mail_template.txt", 'r')

		msg_mail = f.read()
		msg_mail = msg_mail.format(person, file)

		f.close

		return msg_mail

	def read_adress_to(self, person):
		if person in self.config["contacts"]:
			return self.config["contacts"][person]
		else:
			return person
	

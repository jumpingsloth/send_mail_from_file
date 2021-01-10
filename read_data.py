import toml
from os.path import expanduser

class Data:

	def __init__(self):
		config_file = expanduser('~/.send_file/config.toml')
		self.config = toml.load(config_file)
		self.dir = self.config["userconfig"]["directory"]
		self.sent_dir = self.config["userconfig"]["sent_directory"]
		
		self.host = self.config["userconfig"]["host"]
		self.port = self.config["userconfig"]["port"]
		self.adress_from = self.config["userconfig"]["adress"]
		self.password = self.config["userconfig"]["password"]

	def read_template(self, person, file):
		# read mail template from file
		template_file = expanduser('~/.send_file/mail_template.txt')
		msg_mail = ''
		with open(template_file, 'r', encoding='utf-8') as f:
			msg_mail = f.read()
			msg_mail = msg_mail.format(person, file)

		return msg_mail

	def read_adress_to(self, person):
		if person in self.config["contacts"]:
			return self.config["contacts"][person]
		else:
			return person
	

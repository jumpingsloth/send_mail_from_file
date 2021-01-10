import email, smtplib, ssl, os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from read_data import Data

class Send:

	def send_mail(self, adress_to, subject, message, file):
		data = Data()

		filename = os.path.basename(file)

		msg_mail = MIMEMultipart()
		msg_mail["From"] = data.adress_from
		msg_mail["To"] = adress_to
		msg_mail["Subject"] = subject

		msg_mail.attach(MIMEText(message, 'plain'))

		with open(file, "rb") as attachment:
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())

		encoders.encode_base64(part)

		part.add_header(
			"Content-Disposition",
			f"attachment; filename= {filename}"
		)

		msg_mail.attach(part)
		text = msg_mail.as_string()

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(data.host, data.port, context=context) as server:
			server.login(data.adress_from, data.password)
			server.sendmail(data.adress_from, adress_to, text)

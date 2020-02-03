import http.server
import socketserver
from gpapi.googleplay import GooglePlayAPI, LoginError, SecurityCheckError
import random

class TokenDispenser(socketserver.BaseRequestHandler):
	def login(self):
		return random.choice(list(open('passwords/passwords.txt'))).split(" ")

	def setup(self):
		self.api = GooglePlayAPI(locale="en_GB", timezone="CEST", device_codename="bacon")

	def handle(self):
		try:
			self.gmail_address, self.gmail_password = self.login()
			self.api.login(email=self.gmail_address, password=self.gmail_password)
			self.token = self.api.authSubToken
			self.gsfid = hex(self.api.gsfId).replace('0x', '')

			print("Token: {}, gsfId: {}".format(self.token, self.gsfid))
			self.request.sendall(str.encode("HTTP/1.1 200 OK\n\n" + self.token + " " + self.gsfid))
		except (LoginError, SecurityCheckError) as e:
			print("Error: " + str(e))
			self.request.sendall(str.encode("HTTP/1.1 200 OK\n\n" + str(e)))

if __name__ == "__main__":
	socketserver.TCPServer.allow_reuse_address = True # Prevent 'cannot bind to address' errors on restart

	HOST, PORT = "localhost", 8080

	with socketserver.TCPServer((HOST, PORT), TokenDispenser) as server:
		server.serve_forever()
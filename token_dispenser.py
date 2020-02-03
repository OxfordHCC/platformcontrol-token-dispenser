import http.server
import socketserver
from gpapi.googleplay import GooglePlayAPI, LoginError, SecurityCheckError
import configparser

class TokenDispenser(socketserver.BaseRequestHandler):
    def setup(self):
        config = configparser.ConfigParser()
        config.read('gplaycli.conf')

        self.gmail_address      = config.get('Credentials', 'gmail_address', fallback=None)
        self.gmail_password     = config.get('Credentials', 'gmail_password', fallback=None)
        self.device_codename    = config.get('Device', 'codename', fallback='bacon')
        self.locale             = config.get("Locale", "locale", fallback="en_GB")
        self.timezone           = config.get("Locale", "timezone", fallback="CEST")

        self.api = GooglePlayAPI(locale=self.locale, timezone=self.timezone, device_codename=self.device_codename)

    def handle(self):
        try:
            self.api.login(email=self.gmail_address, password=self.gmail_password)
            self.token = self.api.authSubToken
            self.gsfid = hex(self.api.gsfId).replace('0x', '')

            print("Token: {}, gsfId: {}".format(self.token, self.gsfid))
            self.request.sendall(str.encode(self.token + " " + self.gsfid)) # self.data.upper()
        except (LoginError, SecurityCheckError) as e:
            print("Error: " + str(e))
            self.request.sendall(str.encode(str(e)))

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True # Prevent 'cannot bind to address' errors on restart

    HOST, PORT = "localhost", 8080

    with socketserver.TCPServer((HOST, PORT), TokenDispenser) as server:
        server.serve_forever()
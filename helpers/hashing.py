from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)


class Hash():

    def bcrypy(password: str) -> str:
        passHashed = f.encrypt(password.encode('utf-8'))
        return passHashed
class ConnectionAlreadyExsist(Exception):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def __str__(self):
        return f"connecion with phone number {self.phone_number} already exists"

import re
from datetime import datetime

class Alphanumeric:
    def __init__(self, value):
        self.value = str(value)
    def __repr__(self):
        return str(bool(re.match("^[A-Za-z0-9]+$", self.value)))

class Date:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        try:
            datetime.strptime(str(self.value), '%d-%m-%Y')
            return "True"
        except ValueError:
            return "False"

class Country:
    def __init__(self, value):
        self.value = str(value)
    def __repr__(self):
        return str(bool(re.match("^[A-Za-z]", str(self.value))))

class ClosedSetOfOptions:
    def __init__(self, value):
        self.value = str(value)
        print(self.value)
    def __repr__(self):
        #return str(bool(re.match("^\\s*[A-Za-z0-9]+(?:\\s+[A-Za-z0-9]+)*\\s*$", str(self.value))))
        return str(bool(re.match("^\\w+(?:(?:,\\s\\w+)+|(?:\\s\\w+)+)$", str(self.value))))

class Lei:
    def __init__(self, value):
        self.value = str(value)
        print(self.value)
    def __repr__(self):
        return str(bool(re.match("^[0-9]{4}[0]{2}[A-Z0-9]{12}[0-9]{2}$", str(self.value))))

class BinaryOptions:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(bool(re.match("^[Yy].*", self.value) or re.match("^[Nn].*", self.value)))





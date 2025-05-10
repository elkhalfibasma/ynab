# cgi.py - mock version for compatibility
def parse_header(line):
    return line, {}

class MiniFieldStorage:
    def __init__(self, name, value):
        self.name = name
        self.value = value

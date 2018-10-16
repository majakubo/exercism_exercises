from string import ascii_letters as letters
import random
class Robot(object):
    used_names = set()

    def __init__(self):
        self.name = Robot.generate_name()
    def reset(self):
        self.name = Robot.generate_name()
        
    def generate_name():
        while True:
            prefix = random.choice(letters) + random.choice(letters)
            prefix = prefix.upper()
            number = random.randint(100, 999)       
            name = prefix + str(number)
            if not name in Robot.used_names:
                break
        
        Robot.used_names.add(name)
        
        return name

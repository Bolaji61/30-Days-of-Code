class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
    def amIOld(self):
    # Do some computations in here and print out the correct statement to the console
        if self.age < 0:
            print("Age is not valid, setting age to 0.")
            print("You are young.")
        elif 0 < self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        if self.age < 0:
            self.age==0
            self.age+=1
        else:
            pass
        self.age+=1

t = int(input())

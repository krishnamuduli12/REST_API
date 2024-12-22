class Mother:
    def speak(self):
        print("Mother Speaking !!!")

class Father:
    def talking(self):
        print("Father Talking !!!")
        
class Child(Mother, Father):
    pass

child = Child()
child.speak()
child.talking()
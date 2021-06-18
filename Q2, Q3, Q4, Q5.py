#-------------------------------------------------------------QUESTION 2-----------------------------------#
class Speedy:

    def __init__(self, clockRateGHz = 1, noOfCycles = 1):

        self.clockRateGHz = clockRateGHz
        self.noOfCycles = noOfCycles

    def set_clockRateGHz(self):
        self.clockRateGHz = int(input(f"Enter the clocking rate of the computer in gigahertz: "))

    def setNoOfCyccles(self ,n):

        self.noOfCycles = n


    def findTime(self):

        return (f"The time in nanoseconds to execute the no of cycles is: {self.noOfCycles/self.clockRateGHz}")


#-------------------------------------------------------------QUESTION 3-------------------------------------#

class Memorized:

    def __init__(self, type = "Semiconductor", sizeKB = 0):

        self.type = type
        self.sizeKB = sizeKB

    def set_type(self):
        self.type = input(f"Enter the type of the memory of the Computer: ")

    def set_sizeKB(self):
        self.sizeKB = int(input(f"Enter the size of the Memory in KB's: "))

    def sizeMB(self):
        return (f"{self.sizeKB /1024}")

    def printMemory(self):
        print(f"Memory Type: {self.type}\n"
              f"Capacity:\n"
              f"Size in KB's: {self.sizeKB}\n"
              f"Size in MB's: {self.sizeMB()}")

#-------------------------------------------------------------QUESTION 4-------------------------------------#

class Computer(Speedy, Memorized):

    def __init__(self, noOfIOPorts = 0, manufacturer = ""):

        self.noOfIOPorts = noOfIOPorts
        self.manufacturer = manufacturer
        Speedy.__init__(self)
        Memorized.__init__(self)

    def set_noOfIOPorts(self):
        self.noOfIOPorts = int(input(f"Enter the number of IO Ports: "))

    def set_manufacturer(self):
        self.manufacturer = input(f"Enter the name of system's Manufacturer: ")


    def printConfig(self):
        print(f"Configuration\n"
              f"Manufacturer: {self.manufacturer}\n"
              f"Number of IO Ports: {self.noOfIOPorts}\n"
              f"Memory:\n"
              f"Memory Type: {self.type}\n"
              f"Size in KB's: {self.sizeKB}\n"
              f"Size in MB's: {self.sizeMB()}\n"
              f"Speed:"
              f"Takes {self.findTime()} nsec to execute {self.noOfCycles} cycles")


#-------------------------------------------------------------QUESTION 5-------------------------------------#

# TESTING CLASS COMPUTER

c = Computer(20, "DELL")
c.set_clockRateGHz()
c.setNoOfCyccles(10)
c.set_type()
c.set_sizeKB()
c.printConfig()


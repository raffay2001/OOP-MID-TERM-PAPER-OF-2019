#-------------------------------------------------------------QUESTION 7-----------------------------------#
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


#-------------------------------------------------------------QUESTION 7-------------------------------------#

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

#-------------------------------------------------------------QUESTION 7-------------------------------------#

class Computer(Speedy):

    computers = 0

    def __init__(self, noOfIOPorts = 0, manufacturer = ""):

        self.noOfIOPorts = noOfIOPorts
        self.manufacturer = manufacturer
        self.memory_elements = []
        Computer.computers += 1
        self.no_of_computers = Computer.computers
        Speedy.__init__(self)


    def add_memory_element(self):
        choice = int(input(f"How many Memory Elements do you want to input: "))
        for i in range(choice):
            self.memoryElement = Memorized()
            self.memoryElement.set_type()
            self.memoryElement.set_sizeKB()
            self.memory_elements.append(self.memoryElement)

    def set_noOfIOPorts(self):
        self.noOfIOPorts = int(input(f"Enter the number of IO Ports: "))

    def set_manufacturer(self):
        self.manufacturer = input(f"Enter the name of system's Manufacturer: ")


    def printConfig(self):
        print(f"Configuration\n"
              f"Manufacturer: {self.manufacturer}\n"
              f"Number of IO Ports: {self.noOfIOPorts}\n"
              f"Speed:\n"
              f"Takes {self.findTime()} nsec to execute {self.noOfCycles} cycles")
        count = 1
        for item in self.memory_elements:
            print(f"Memory Element {count}:")
            (item.printMemory())
            print(f"------------------------------------")
            count += 1

    def total_memory_elements(self):
        return f"The Total Number of Memory Elements are: {len(self.memory_elements)}"

    def total_computers(self):
        print(f"The Total Number of Computer Instances are: {self.no_of_computers}")


#-------------------------------------------------------------QUESTION 7-------------------------------------#

# TESTING CLASS COMPUTER

c = Computer(20, "DELL")
c.set_clockRateGHz()
c.setNoOfCyccles(10)
c.add_memory_element()
c.printConfig()
print(c.total_memory_elements())

c1 = Computer(30, "HP")
c1.total_computers()


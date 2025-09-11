class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
    def turnOn(self):
        self.swtichIsOn = True
    def turnOff(self):
        self.switchIsOn = False
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1
    def show(self):
        print(self.switchIsOn)
        print(self.brightness)

def main():
    d0 = DimmerSwitch()
    d0.show()
    d0.turnOn()
    d0.raiseLevel()
    d0.show()
    
main()

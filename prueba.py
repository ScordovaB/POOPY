class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("En circulacion el "+ self.make +" "+self.model+ " Del año "+self.year +" y es del color "+ self.color)
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("En circulacion el "+ self.make +" "+self.model+ " Del año "+self.year)
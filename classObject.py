class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    def start(self):
        print("Starting")
    
    def stop(self):
        print("Stopping")

    def getDetails(self):
        return {"name": self.name, "brand": self.brand}

class Bike():
    def __init__(self,Bike_name,Bike_colour,Bike_mileage):
        self.a=Bike_name
        self.b=Bike_colour
        self.c=Bike_mileage
    def Data(self):
       print("Bike_name:",self.a)
       print("Bike_colour:",self.b)
       print("Bike_mileage:",self.c)
       
Bike_obj=Bike("KTM","Black","6000MAH")
Bike_obj.Data()


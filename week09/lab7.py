class Vehicle:
    def __init__(self, vid, model, year):
        self.vid=vid
        self.model=model
        self.year=year

    def __str__(self):
        return "Vehicle id is " +str(self.vid) + " vehicle model is " + str(self.model) + " year is " + str(self.year)

    def __eq__(self, other):
        return self.vid==other.vid

    def is_new(self,n):
        return self.year>=(2026-n)

class Car(Vehicle):
    def __init__(self, vid, model, year,fuel_type,doors):
        super().__init__(vid,model,year)
        self.fuel_type=fuel_type
        self.doors=doors

    def __str__(self):
        return f"[Car]        VID: {self.vid} | {self.model:<15} ({self.year}) | Fuel: {self.fuel_type:<8} | {self.doors} Doors"

class Truck(Vehicle):
    def __init__(self, vid, model, year,max_load,axles):
        super().__init__(vid,model,year)
        self.max_load=max_load
        self.axles=axles

    def __str__(self):
        return f"[Truck]      VID: {self.vid} | {self.model:<15} ({self.year}) | Load: {self.max_load}kg  | {self.axles} Axles"

class Motorcycle(Vehicle):
    def __init__(self, vid, model, year,engine_cc,type):
        super().__init__(vid,model,year)
        self.engine_cc=engine_cc
        self.type=type

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model:<15} ({self.year}) | Eng: {self.engine_cc}cc     | Type: {self.type}"

def save_fleet_to_file(vehicles,filename):
     with open(filename,"w") as f:
         for v in vehicles:
             if isinstance(v,Car):
                f.write(f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}\n")
             elif isinstance(v, Truck):
                f.write(f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}\n")
             elif isinstance(v, Motorcycle):
                f.write(f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.type}\n")


def load_fleet_from_file(filename):
    vehicles = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = [p.strip() for p in line.strip().split(',')]
                v_type = parts[0]
                if v_type == 'Car':
                    vehicles.append(Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
                elif v_type == 'Truck':
                    vehicles.append(Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5])))
                elif v_type == 'Motorcycle':
                    vehicles.append(Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5]))
    except FileNotFoundError:
        print("File not found.")
    return vehicles

if __name__=="__main__":
    car1=Car("t1","passat", 2020, "Electric",4)
    car2=Car("m2","BMW",2003,"mazot",4+1)
    truck1=Truck( "v3","mercedes", 2025,40000, 6)
    truck2=Truck("h4","Man",2026,42000, 6)
    motor1=Motorcycle("m5","Yamaha",2021,1200, "sport")
    motor2=Motorcycle("y6","Orhan",2023,800, "pancar motoru")

    fleet = [car1, car2, truck1, truck2, motor1, motor2]


    save_fleet_to_file(fleet, "fleet.txt")

    # Araçları dosyadan geri yükleme [cite: 34]
    print(f"Loading fleet data from 'fleet.txt'...")
    loaded_fleet = load_fleet_from_file("fleet.txt")
    print(f"{len(loaded_fleet)} vehicles loaded successfully.")


    print("\nAll Vehicles ---")
    for v in loaded_fleet:
        print(v)


    print("\n--- Recent Vehicles (Last 4 Years) ---")
    for v in loaded_fleet:
        if v.is_new(4):
            print(v)

    print("\n--- Electric Cars Only ---")
    for v in loaded_fleet:
        if isinstance(v, Car) and v.fuel_type == "Electric":
            print(v)




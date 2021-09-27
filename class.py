class batsman:
    def __init__(self, name, age, runs):
        self.name = name
        self.age = age
        self.runs = runs

    def print_name(self):
        print("Name: " + self.name) 
        print("age: " + str(self.age))  
        print("Runs: " + str(self.runs))

hari = batsman("Hari ", 32, 100)       
vasan = batsman("Vasan ", 34, 60) 

hari.print_name()
vasan.print_name()

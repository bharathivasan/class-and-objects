class batsman:
    def __init__(self, name, age, runs):
        self.name = name
        self.age = age
        self.runs = runs

    def print_name(self):
        print("Name: " + self.name) 
        print("age: " + str(self.age))  
        print("Runs: " + str(self.runs))

bharathi = batsman("Bharathi ", 32, 100)       
vasan = batsman("Vasan ", 34, 60) 

bharathi.print_name()
vasan.print_name()

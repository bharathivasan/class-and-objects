class batsman:
    def __init__(self, name, age, runs):
        self.name = name
        self.age = age
        self.runs = runs

    def print_name(self):
        print("Name: " + self.name) 
        print("age: " + str(self.age))  
        print("Runs: " + str(self.runs))

kholi = batsman("Virat kholi", 32, 100)       
rohit = batsman("Rohit sharma", 34, 60) 

kholi.print_name()
rohit.print_name()

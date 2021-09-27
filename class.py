class batsman:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

kholi = batsman("Virat kholi", 32, 100)        
dhoni = batsman("Dhoni", 40, 60) 
print(kholi.name)
print(dhoni.name)